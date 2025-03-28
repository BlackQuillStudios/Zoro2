# chatbot.py
import os
import logging
import re
import base64
from io import BytesIO
from PIL import Image # Requires 'pip install Pillow'
from dotenv import load_dotenv
from google import generativeai as genai
from google.generativeai import types
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# --- Load Environment Variables ---
load_dotenv()

# --- Configuration ---
API_KEY = os.environ.get("GEMINI_API_KEY")
IMAGE_GEN_MODEL = "gemini-2.0-flash-exp-image-generation" # Use a capable model that supports image gen function calls
# If you have specific access to the experimental image generation model:
# IMAGE_GEN_MODEL = "gemini-2.0-flash-exp-image-generation" # Model specifically for image gen call example
# Or more commonly, you'd use function calling with a multimodal model like 1.5 Pro/Flash

DEFAULT_CHAT_MODEL = "gemini-1.5-flash-latest"
DEFAULT_TITLE_MODEL = "gemini-1.5-flash-latest"

# Updated System Instruction with specific tool call format
SYSTEM_INSTRUCTION_CHAT = """You are Zoro, a helpful and respectful personal AI assistant for Blake C.
You should call him 'Sir' and always respond with politeness.

TOOL USE:
- You have access to an image generation tool called 'imagen'.
- Purpose: Generates an image based on the provided text prompt.
- Invocation: If Sir asks you to create, draw, generate, or show an image, or if a visual representation would significantly aid your explanation, you MUST call the 'imagen' tool by outputting the specific string: tool_call(imagen"YOUR_DETAILED_PROMPT_HERE")
- Example Request: "Sir, could you generate an image of a futuristic cityscape at sunset?"
- Your Output: tool_call(imagen"Futuristic cityscape showing tall, sleek buildings with flying vehicles, vibrant greenery integrated, during a colorful sunset with orange and purple hues.")
- Provide a detailed and descriptive prompt within the quotes.
- Do NOT add any other text before or after the tool_call string. The tool call string IS YOUR ENTIRE RESPONSE when generating an image.
- Do NOT try to invent other tools. Only use 'imagen'.
"""

SYSTEM_INSTRUCTION_TITLE = """Analyze the following user query and AI response. Generate a very concise, descriptive title (max 5 words) for this conversation topic. RULES: Output ONLY the title text. Do NOT include introductory phrases. Do NOT add quotation marks. Do NOT add commentary."""

SAFETY_SETTINGS = { HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE, HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE, }

# --- Google AI Configuration ---
genai_configured = False
try:
    if not API_KEY:
        logging.warning("GEMINI_API_KEY not found.")
    else:
        genai.configure(api_key=API_KEY)
        genai_configured = True
        logging.info("Google AI configured successfully with API Key.")
except Exception as e:
    logging.error(f"Error configuring Google AI with API Key: {e}", exc_info=True)

# --- NEW Image Generation Function ---
def generate_image(prompt: str) -> dict | None:
    """
    Generates an image using the specified image generation model.

    Args:
        prompt: The text prompt for image generation.

    Returns:
        A dictionary containing 'image_base64' (base64 encoded PNG) on success,
        or 'error' on failure, or None if AI not configured.
    """
    if not genai_configured:
        logging.error("Image generation skipped: AI service not configured.")
        return {"error": "Image generation service not configured."}

    logging.info(f"Attempting image generation with prompt: '{prompt[:60]}...' using model {IMAGE_GEN_MODEL}")

    try:
        # --- Using the specific image generation model approach ---
        # Ensure client uses the globally configured API key
        # Note: genai.Client() might not be needed if genai.configure() is used globally.
        # Using genai.generate_text or similar with the right model might be simpler.
        # However, aligning with the user's original example structure:

        # Re-create client instance if necessary, or rely on global config
        # client = genai.Client() # This might re-read env vars, ensure it uses the configured key

        # Use the globally configured genai module if possible
        response = genai.generate_content(
            model=IMAGE_GEN_MODEL, # Use the specific image gen model from config
            prompt=prompt,         # Pass only the prompt
            # The original example used 'contents=prompt', API might expect 'prompt='
            # config=types.GenerateContentConfig(response_modalities=['Image']) # Request image only - May not be needed or correct syntax depending on model/method
            # Simpler approach: Let the model handle the response type based on its capabilities
        )

        # Process the response to find image data
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                # Gemini 1.5 Flash/Pro might return FunctionResponse or Blob directly
                if hasattr(part, 'inline_data') and part.inline_data is not None: # Check for inline_data structure
                    img_bytes = part.inline_data.data
                    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
                    logging.info("Image generated successfully (inline_data).")
                    return {"image_base64": img_base64}
                # Add checks for other potential image data structures if needed
                # based on the specific model's response format (e.g., blob, function response)

        logging.warning("Image generation response did not contain expected image data.")
        # Check for blocking
        if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
            block_reason = response.prompt_feedback.block_reason
            logging.warning(f"Image generation blocked: {block_reason}")
            return {"error": f"Image generation blocked due to safety filters ({block_reason})."}

        return {"error": "Failed to generate image (no image data in response)."}

    except Exception as e:
        logging.error(f"Error during image generation with model '{IMAGE_GEN_MODEL}': {e}", exc_info=True)
        error_msg = f"Image generation failed: {type(e).__name__}."
        if "resource not found" in str(e).lower():
            error_msg += f" Model '{IMAGE_GEN_MODEL}' may be invalid or inaccessible."
        return {"error": error_msg}


# --- Core Chatbot Logic (MODIFIED to check for tool call) ---
def get_ai_response(user_input: str, model_name: str | None = None, system_instruction: str | None = None) -> str | dict:
    """
    Gets a response OR detects an image generation tool call.

    Returns:
        str: The generated text response.
        dict: A dictionary indicating image generation result (e.g., {'image_base64': ...} or {'error': ...}).
    """
    if not genai_configured:
        logging.error("Chat skipped: AI service not configured.")
        return "Sir, I apologize, but my connection to the AI service (Configuration Error) is not working correctly."

    effective_model_name = model_name or DEFAULT_CHAT_MODEL
    effective_system_instruction = system_instruction if system_instruction is not None else SYSTEM_INSTRUCTION_CHAT

    logging.info(f"Generating chat response using model: {effective_model_name}")
    if effective_system_instruction != SYSTEM_INSTRUCTION_CHAT:
         logging.info(f"Using custom system instruction (length: {len(effective_system_instruction)})")

    try:
        model = genai.GenerativeModel(
            effective_model_name,
            safety_settings=SAFETY_SETTINGS,
            system_instruction=effective_system_instruction
        )

        # Use generate_content directly for simpler tool call detection (non-streaming)
        response = model.generate_content(user_input)

        # Check for standard text response first
        try:
            raw_text_response = response.text.strip()
        except ValueError: # Handle cases where response might just be function call, no .text
             raw_text_response = ""
        except Exception as e:
             logging.warning(f"Could not get .text from response: {e}")
             raw_text_response = "" # Treat as empty if error accessing .text

        # *** Check for the specific tool call string ***
        tool_call_match = re.match(r'^\s*tool_call\(imagen"(.+)"\)\s*$', raw_text_response, re.DOTALL | re.IGNORECASE) # Ignore case maybe safer

        if tool_call_match:
            image_prompt = tool_call_match.group(1).strip()
            # Basic prompt validation (optional)
            if not image_prompt:
                 logging.warning("Detected imagen tool call but prompt was empty.")
                 return "Sir, you asked for an image, but didn't provide a description. Please try again."

            logging.info(f"Detected imagen tool call with prompt: '{image_prompt[:60]}...'")
            # Call the image generation function
            image_result = generate_image(image_prompt)
            return image_result if image_result else {"error": "Image generation function returned an unexpected error."}

        elif raw_text_response:
            # It's a regular text response
             return raw_text_response
        else:
            # Handle empty or blocked response if no tool call detected and no .text
            reason = "Unknown reason (empty response)"
            is_blocked = False
            try:
                 final_feedback = response.prompt_feedback
                 if final_feedback.block_reason: reason = f"Safety guidelines ({final_feedback.block_reason})"; is_blocked = True
                 logging.warning(f"Chat model '{effective_model_name}' returned empty response. Reason: {reason}")
                 if is_blocked: return f"Sir, I'm unable to process that request due to {reason}."
                 else: return "Sir, I received an empty response. Could you please try rephrasing?"
            except Exception as feedback_error:
                 logging.warning(f"Empty chat response, couldn't get feedback: {feedback_error}")
                 return "Sir, I received an empty response. Could you please try rephrasing?"

    # --- (Keep existing exception handling) ---
    except Exception as e:
        logging.error(f"Error during AI chat generation with '{effective_model_name}': {e}", exc_info=True)
        error_detail = f"Could not access model '{effective_model_name}'." if "resource not found" in str(e).lower() or "permission denied" in str(e).lower() else f"Internal error ({type(e).__name__})."
        return f"Sir, I encountered an error trying to use the selected AI model. {error_detail} Please check settings or server logs."


# --- Title Generation Logic (Keep as is) ---
def get_ai_title(user_message: str, ai_response: str, model_name: str | None = None) -> str | None:
     if not genai_configured: return None
     effective_model_name = model_name or DEFAULT_TITLE_MODEL
     logging.info(f"Generating title using model: {effective_model_name}")
     prompt = f'User Query:\n"{user_message}"\n\nAI Response:\n"{ai_response}"\n\nGenerate Title:'
     try:
         title_model_instance = genai.GenerativeModel(effective_model_name, safety_settings=SAFETY_SETTINGS, system_instruction=SYSTEM_INSTRUCTION_TITLE)
         response = title_model_instance.generate_content(prompt)
         if not response.candidates: return None
         first_candidate = response.candidates[0]
         if not hasattr(first_candidate, 'content') or not hasattr(first_candidate.content, 'parts') or not first_candidate.content.parts: return None
         generated_title = response.text.strip()
         if not generated_title: return None
         generated_title = re.sub(r'^["\']+|["\']+$', '', generated_title); generated_title = re.sub(r'^(Title:|Here is the title:)\s*', '', generated_title, flags=re.IGNORECASE)
         MAX_TITLE_WORDS = 7; title_words = generated_title.split();
         if len(title_words) > MAX_TITLE_WORDS: generated_title = " ".join(title_words[:MAX_TITLE_WORDS]) + "..."
         if not generated_title: return None
         logging.info(f"Generated title: '{generated_title}'")
         return generated_title
     except Exception as e: logging.error(f"Error during AI title generation: {e}", exc_info=True); return None


# --- Optional: Testing Block ---
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Chatbot Module Test Mode (using default model/instructions).")
    # Test Chat
    test_user_msg = "Sir, explain quantum entanglement like I'm five."
    print(f"\nTesting Chat Response for: '{test_user_msg}'")
    ai_resp = get_ai_response(test_user_msg)
    if isinstance(ai_resp, str) and ai_resp and not ai_resp.startswith("Sir, I apologize") and not ai_resp.startswith("Sir, I encountered"):
        print(f"\nZoro Response:\n{ai_resp}")
        # Test Title
        print(f"\nTesting Title Generation for:")
        print(f"  User: {test_user_msg}")
        print(f"  AI: {ai_resp[:100]}...")
        title = get_ai_title(test_user_msg, ai_resp)
        if title: print(f"\n---> Generated Title: '{title}'")
        else: print("\n---> Title generation failed or returned None.")
    elif isinstance(ai_resp, dict):
         print(f"\nZoro Response was an Image Gen Result:\n{ai_resp}") # Should not happen for this prompt
    else:
        print(f"\nZoro Response indicates error:\n{ai_resp}")
        print("\nSkipping title generation due to chat response error.")

    # Test Image Gen directly (if prompt detected)
    test_user_img_msg = 'Hey Zoro, can you make an image for me? tool_call(imagen"A cute kitten wearing a party hat")'
    print(f"\nTesting Image Response for: '{test_user_img_msg}'")
    img_result = get_ai_response(test_user_img_msg)
    if isinstance(img_result, dict):
         if "image_base64" in img_result:
             print("\n---> Image generation SUCCEEDED (received base64 data).")
             # Optional: Save/show image if running locally
             # try:
             #     img_data = base64.b64decode(img_result['image_base64'])
             #     img = Image.open(BytesIO(img_data))
             #     img.save("test_generated_image.png")
             #     print("     Test image saved as test_generated_image.png")
             # except Exception as e:
             #     print(f"     Error saving/showing test image: {e}")
         elif "error" in img_result:
             print(f"\n---> Image generation FAILED: {img_result['error']}")
    elif isinstance(img_result, str):
         print(f"\n---> Expected image gen, but got text response:\n{img_result}")
    else:
         print("\n---> Unexpected result type for image gen test.")