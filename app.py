# app.py
import os
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Import the custom module that contains AI logic
import chatbot

# --- Basic Configuration ---
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
log = logging.getLogger(__name__)

# --- Flask App Initialization ---
app = Flask(__name__)

# --- Flask Routes ---

@app.route("/")
def index():
    """Renders the main chat page (index.html)."""
    log.info("Serving index page.")
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    """Handles chat messages, gets AI response using specified model/instructions."""
    try:
        if not request.is_json:
            log.warning("Received non-JSON request to /chat")
            return jsonify({"error": "Request must be JSON"}), 415

        data = request.get_json()
        user_message = data.get("message")
        # *** Extract model and instructions from request ***
        model_name = data.get("model_name") # Will be None if not sent
        system_instruction = data.get("system_instruction") # Will be None if not sent or empty

        if not user_message:
            log.warning("Received /chat request with no 'message' field.")
            return jsonify({"error": "No message provided."}), 400

        log.info(f"Received message for /chat: '{user_message[:60]}...'")
        log.info(f"Requested Model: {model_name or 'Default'}, Instructions Provided: {'Yes' if system_instruction is not None else 'No'}")

        # *** Pass extracted params to chatbot function ***
        ai_response = chatbot.get_ai_response(
            user_input=user_message,
            model_name=model_name,
            system_instruction=system_instruction
        )

        log.info(f"Sending chat response: '{str(ai_response)[:100]}...'")
        return jsonify({"response": ai_response})

    except Exception as e:
        log.error(f"Error in /chat route: {e}", exc_info=True)
        return jsonify({"error": "An internal server error occurred processing the chat message."}), 500

@app.route("/generate-title", methods=["POST"])
def generate_title_route():
    """Handles request to generate a chat title using specified model."""
    try:
        if not request.is_json:
            log.warning("Received non-JSON request to /generate-title")
            return jsonify({"error": "Request must be JSON"}), 415

        data = request.get_json()
        user_message = data.get("user_message")
        ai_response = data.get("ai_response")
        # *** Extract model name from request ***
        model_name = data.get("model_name") # Will be None if not sent

        if not user_message or not ai_response:
            log.warning("Received /generate-title request missing 'user_message' or 'ai_response'.")
            return jsonify({"error": "Missing required message content for title generation."}), 400

        log.info(f"Received request for /generate-title. Requested Model: {model_name or 'Default'}")

        # *** Pass extracted model name to chatbot function ***
        generated_title = chatbot.get_ai_title(
            user_message=user_message,
            ai_response=ai_response,
            model_name=model_name
        )

        if generated_title:
            log.info(f"Sending generated title: '{generated_title}'")
            return jsonify({"title": generated_title})
        else:
            log.warning("Title generation in chatbot module returned None or failed.")
            return jsonify({"title": None, "message": "Could not generate title."}), 200

    except Exception as e:
        log.error(f"Error in /generate-title route: {e}", exc_info=True)
        return jsonify({"error": "An internal server error occurred during title generation."}), 500


# --- Run the App ---
if __name__ == "__main__":
    log.info("Starting Flask development server...")
    app.run(debug=True, host='0.0.0.0', port=5000) # Use debug=False in production!