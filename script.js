// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    // --- Selectors (Keep all existing) ---
    const chatbox = document.getElementById('chatbox');
    // ... and all others ...
    const chatHeaderTitle = document.getElementById('chatHeaderTitle'); // Ensure selector exists
    const themeStylesheet = document.getElementById('themeStylesheet'); // Ensure selector exists


    // --- State Variables (Keep all existing) ---
    // ... currentChatId, allChats, openDropdownId, etc ...
    let currentSystemInstruction = `You are Zoro, a helpful and respectful personal AI assistant for Blake C.\nYou should call him 'Sir' and always respond with politeness.`; // Default instructions


    // --- Constants (Keep existing) ---
    // ... INITIAL_GREETING_TEXT, etc ...

    // --- Utility, LocalStorage, Dropdown, Rename/Delete, Theme, Model Functions ---
    // ... (Keep ALL these functions as they were) ...
    // generateUUID, getTimestamp, generateDefaultChatTitle
    // loadChatsFromLocalStorage, saveChatsToLocalStorage
    // closeOpenDropdown, toggleDropdown, handleRenameChat, handleDeleteChat
    // openSettingsPopup, closeSettingsPopup
    // handleThemeChange, loadSavedTheme
    // handleModelChange, loadSavedModel
    // handleCopyCodeClick


    // --- Configure Marked.js and Highlight.js (Keep as is) ---
    marked.setOptions({ highlight: function(code, lang) { const language = hljs.getLanguage(lang) ? lang : 'plaintext'; try { return hljs.highlight(code, { language, ignoreIllegals: true }).value; } catch (error) { console.error("Highlight.js error:", error, "Lang:", lang); return hljs.highlight(code, { language: 'plaintext', ignoreIllegals: true }).value; } }, breaks: true, gfm: true, });


    // --- UI Update Functions ---

    // *** MODIFIED to handle potential image data or error message ***
    function addMessageToDOM(message) {
        // message object might have { sender, text } OR { sender, image_base64 } OR { sender, image_error }
        if (!chatbox) return;
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', message.sender === 'user' ? 'user-message' : 'ai-message');
        const iconDiv = document.createElement('div');
        iconDiv.classList.add('message-icon');
        iconDiv.textContent = message.sender === 'user' ? 'Y' : 'Z';
        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');

        if (message.image_base64) {
            // --- Handle Image ---
            const imgElement = document.createElement('img');
            imgElement.src = message.image_base64; // Base64 data URI
            imgElement.alt = "Generated Image"; // Add descriptive alt text later if possible
            contentDiv.appendChild(imgElement);
            // Optionally add text if the backend ever sends text alongside image
            if (typeof message.text === 'string' && message.text.trim() !== '') {
                const textParagraph = document.createElement('p');
                 // Parse potential markdown in accompanying text too
                 textParagraph.innerHTML = marked.parse(message.text.trim());
                 contentDiv.insertBefore(textParagraph, imgElement); // Put text before image
            }
        } else if (message.image_error) {
             // --- Handle Image Generation Error ---
             const errorParagraph = document.createElement('p');
             // Display error politely, maybe wrap in italics or specific style
             errorParagraph.innerHTML = `<i>Sir, I encountered an issue generating the image: ${message.image_error}</i>`;
             contentDiv.appendChild(errorParagraph);
        } else {
            // --- Handle Regular Text / Markdown ---
            const messageText = typeof message.text === 'string' ? message.text : '';
            const convertedHtml = marked.parse(messageText); // Parse Markdown
            contentDiv.innerHTML = convertedHtml;

            // Post-processing: Add Code Block Headers
            contentDiv.querySelectorAll('pre code').forEach((codeBlock) => {
                const preElement = codeBlock.parentElement;
                if (preElement && preElement.tagName === 'PRE' && !preElement.querySelector('.code-block-header')) {
                    let language = 'plaintext';
                    const classes = codeBlock.className.split(' ');
                    const langClass = classes.find(cls => cls.startsWith('language-'));
                    if (langClass) { language = langClass.replace('language-', ''); }
                    const headerDiv = document.createElement('div'); headerDiv.className = 'code-block-header';
                    const langSpan = document.createElement('span'); langSpan.className = 'code-block-language'; langSpan.textContent = language;
                    const copyButton = document.createElement('button'); copyButton.className = 'copy-code-button'; copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy';
                    copyButton.dataset.code = codeBlock.textContent;
                    headerDiv.appendChild(langSpan); headerDiv.appendChild(copyButton);
                    preElement.insertBefore(headerDiv, codeBlock);
                }
            });
        }

        // Append icon and content in correct order
        if (message.sender === 'user') { messageDiv.appendChild(contentDiv); messageDiv.appendChild(iconDiv); }
        else { messageDiv.appendChild(iconDiv); messageDiv.appendChild(contentDiv); }
        chatbox.appendChild(messageDiv);
    }


    function loadChatMessages(chatId) { /* ... keep existing ... */ const chat = allChats.find(c => c.id === chatId); if (!chatbox) return; chatbox.innerHTML = ''; if (chat && chat.messages) { chat.messages.forEach(addMessageToDOM); if (chatHeaderTitle) chatHeaderTitle.textContent = chat.title || "Chat"; } else { addMessageToDOM(INITIAL_GREETING_MSG_OBJ); if (chatHeaderTitle) chatHeaderTitle.textContent = "Zoro - Personal AI Assistant"; } requestAnimationFrame(() => { if(chatbox) chatbox.scrollTop = chatbox.scrollHeight; }); }
    function updateSidebar() { /* ... keep existing ... */ if (!chatList) return; const fragment = document.createDocumentFragment(); if (allChats.length === 0) { const placeholder = document.createElement('li'); placeholder.className = 'no-chats-placeholder'; placeholder.style.cssText = 'text-align: center; padding: 20px; color: var(--text-medium); font-style: italic; font-size: 0.9em; cursor: default;'; placeholder.textContent = 'No chats yet.'; fragment.appendChild(placeholder); } else { allChats.forEach(chat => { const listItem = document.createElement('li'); listItem.className = 'chat-list-item'; listItem.dataset.chatId = chat.id; const titleSpan = document.createElement('span'); titleSpan.className = 'chat-title'; titleSpan.textContent = chat.title || 'Chat'; listItem.appendChild(titleSpan); const optionsButton = document.createElement('button'); optionsButton.className = 'chat-options-button'; optionsButton.innerHTML = '<i class="fa-solid fa-ellipsis"></i>'; optionsButton.dataset.chatId = chat.id; listItem.appendChild(optionsButton); const dropdown = document.createElement('div'); dropdown.className = 'chat-options-dropdown'; dropdown.id = `dropdown-${chat.id}`; const renameButton = document.createElement('button'); renameButton.className = 'rename-chat-button'; renameButton.dataset.chatId = chat.id; renameButton.innerHTML = '<i class="fa-solid fa-pencil"></i> Rename'; dropdown.appendChild(renameButton); const deleteButton = document.createElement('button'); deleteButton.className = 'delete-chat-button'; deleteButton.dataset.chatId = chat.id; deleteButton.innerHTML = '<i class="fa-solid fa-trash-can"></i> Delete'; dropdown.appendChild(deleteButton); listItem.appendChild(dropdown); if (chat.id === currentChatId) { listItem.classList.add('active-chat'); } fragment.appendChild(listItem); }); } chatList.innerHTML = ''; chatList.appendChild(fragment); }
    function activateChat(chatId) { /* ... keep existing ... */ if (!chatId) return; closeOpenDropdown('activateChat'); currentChatId = chatId; loadChatMessages(chatId); updateSidebar(); if (userInput) userInput.focus(); }
    function showLoading(isLoading) { /* ... keep existing ... */ if (userInput) userInput.disabled = isLoading; if (sendButton) { sendButton.disabled = isLoading; sendButton.innerHTML = isLoading ? '<i class="fa-solid fa-spinner fa-spin"></i>' : '<i class="fa-solid fa-paper-plane"></i>'; } }

    // --- AI Title Generation ---
    async function fetchAndSetAiTitle(chatId, userMessageText, aiResponseText) { /* ... keep existing ... */ console.log(`Attempting to generate AI title for chat: ${chatId} using model: ${currentSelectedModel}`); let needsDefaultFallback = false; if (!userMessageText || !aiResponseText || aiResponseText.includes("apologize") || aiResponseText.includes("error")) { console.warn("Skipping AI title generation due to potentially empty/error initial messages."); needsDefaultFallback = true; } if (!needsDefaultFallback) { try { const response = await fetch('/generate-title', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ user_message: userMessageText, ai_response: aiResponseText, model_name: currentSelectedModel }), }); if (!response.ok) { console.error(`Error fetching title (${response.status}): ${response.statusText}`); needsDefaultFallback = true; } else { const data = await response.json(); if (data && data.title) { const generatedTitle = data.title; console.log(`Received AI title: "${generatedTitle}" for chat ${chatId}`); const chatIndex = allChats.findIndex(c => c.id === chatId); if (chatIndex !== -1) { if (allChats[chatIndex].title !== generatedTitle) { allChats[chatIndex].title = generatedTitle; saveChatsToLocalStorage(); updateSidebar(); if (currentChatId === chatId && chatHeaderTitle) chatHeaderTitle.textContent = generatedTitle; } return; } else { console.warn(`Chat ${chatId} not found when setting AI title.`); } } else { console.warn("AI title generation returned no title.", data); needsDefaultFallback = true; } } } catch (error) { console.error("Network error during AI title generation:", error); needsDefaultFallback = true; } } if (needsDefaultFallback) { const chatIndex = allChats.findIndex(c => c.id === chatId); if (chatIndex !== -1 && allChats[chatIndex].title === "New Chat") { const defaultTitle = generateDefaultChatTitle(userMessageText); if (allChats[chatIndex].title !== defaultTitle) { allChats[chatIndex].title = defaultTitle; saveChatsToLocalStorage(); updateSidebar(); if (currentChatId === chatId && chatHeaderTitle) chatHeaderTitle.textContent = defaultTitle; console.log(`Used default title: "${defaultTitle}"`); } } } }

    // --- Main Chat Functionality (MODIFIED to handle different response types) ---
    async function sendMessage() {
        if (!userInput || !currentChatId) return;
        const messageText = userInput.value.trim();
        if (!messageText) return;
        console.log(`Sending message using model: ${currentSelectedModel}`);
        const userMessage = { sender: 'user', text: messageText, timestamp: getTimestamp() };
        addMessageToDOM(userMessage); // Display user message
        userInput.value = '';
        showLoading(true);
        if (chatbox) requestAnimationFrame(() => { chatbox.scrollTop = chatbox.scrollHeight; });
        const currentChatIndex = allChats.findIndex(c => c.id === currentChatId);
        if (currentChatIndex === -1) { console.error("Critical: Current chat not found!"); showLoading(false); return; }
        const isFirstUserExchange = allChats[currentChatIndex].messages.length === 1;
        allChats[currentChatIndex].messages.push(userMessage);
        allChats[currentChatIndex].timestamp = getTimestamp();
        saveChatsToLocalStorage();

        let responseData = null; // To store the parsed JSON response
        let errorMessage = null; // To store specific error messages

        try { // --- Fetch Response from Backend ---
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: messageText,
                    model_name: currentSelectedModel,
                    system_instruction: currentSystemInstruction
                 }),
            });

            if (!response.ok) {
                 errorMessage = `Sir, there was a server error (Status: ${response.status}).`;
                 try { responseData = await response.json(); if(responseData && responseData.error) errorMessage = `Sir, an error occurred: ${responseData.error}`; } catch(e){} // Ignore parsing error on error response
                 console.error('Error fetching AI response:', response.statusText);
            } else {
                responseData = await response.json(); // Parse successful response
            }

            // --- Process Backend Response ---
            let aiMessageObject = null; // To store the object for history/DOM

            if (errorMessage) { // If fetch failed or backend sent error in payload
                 aiMessageObject = { sender: 'ai', text: errorMessage, timestamp: getTimestamp() };
            } else if (responseData?.image_base64) { // Check for image
                 aiMessageObject = { sender: 'ai', image_base64: responseData.image_base64, timestamp: getTimestamp() };
                 // Optionally add text if included: aiMessageObject.text = responseData.text_accompanying_image || '';
            } else if (responseData?.image_error) { // Check for image error
                 aiMessageObject = { sender: 'ai', image_error: responseData.image_error, timestamp: getTimestamp() };
            } else if (responseData?.response) { // Check for regular text response
                 aiMessageObject = { sender: 'ai', text: responseData.response, timestamp: getTimestamp() };
            } else { // Unexpected success response format
                 errorMessage = "Sir, I received an unexpected response format from the server.";
                 console.warn("Received OK status but unexpected data:", responseData);
                 aiMessageObject = { sender: 'ai', text: errorMessage, timestamp: getTimestamp() };
            }

            // Add the determined AI message/image/error to DOM
            addMessageToDOM(aiMessageObject);
            if (chatbox) requestAnimationFrame(() => { chatbox.scrollTop = chatbox.scrollHeight; });

            // --- Save to History and Handle Title Gen ---
            const updatedChatIndex = allChats.findIndex(c => c.id === currentChatId);
            if (updatedChatIndex !== -1) {
                // Save AI response/image to history IF it wasn't a fetch/server error
                if (!errorMessage && !responseData?.image_error) { // Don't save explicit errors? Or maybe do? Your choice.
                    allChats[updatedChatIndex].messages.push(aiMessageObject);
                    allChats[updatedChatIndex].timestamp = getTimestamp();
                    saveChatsToLocalStorage();

                    // Trigger title gen only on first valid text response
                    if (isFirstUserExchange && aiMessageObject.text) {
                         fetchAndSetAiTitle(currentChatId, messageText, aiMessageObject.text);
                    }
                 } else {
                      console.log("Skipping saving AI error message to history.");
                 }
                 updateSidebar(); // Update sidebar for timestamp sort / potential title change
            } else { console.error("Critical: Current chat lost after AI response!"); }

        } catch (error) { // --- Handle Network Error ---
            const errorMsg = 'Sir, I seem to be unable to connect. Please check the network connection and try again.';
            addMessageToDOM({ sender: 'ai', text: errorMsg, timestamp: getTimestamp() });
            if (chatbox) requestAnimationFrame(() => { chatbox.scrollTop = chatbox.scrollHeight; });
            console.error('Network error during chat fetch:', error);
            updateSidebar(); // Update timestamp maybe?
        } finally {
            showLoading(false);
        }
    }


    // --- Popup Handling Functions ---
    function openSettingsPopup() { /* ... keep existing ... */ closeOpenDropdown('openSettingsPopup'); if (popupOverlay && settingsPopup) { popupOverlay.classList.add('show'); settingsPopup.classList.add('show'); } else { console.error("Popup overlay or settings popup element not found!"); } }
    function closeSettingsPopup() { /* ... keep existing ... */ if (popupOverlay && settingsPopup) { popupOverlay.classList.remove('show'); settingsPopup.classList.remove('show'); } }

    // --- Theme Handling ---
    function handleThemeChange(event) { /* ... keep existing ... */ const selectedTheme = event.target.value; if (themeStylesheet) { const newHref = `/static/themes/${selectedTheme}.css`; themeStylesheet.setAttribute('href', newHref); localStorage.setItem(THEME_STORAGE_KEY, selectedTheme); console.log(`Theme stylesheet changed to: ${newHref}`); } else { console.error("Theme stylesheet link element not found!"); } }
    function loadSavedTheme() { /* ... keep existing ... */ const savedTheme = localStorage.getItem(THEME_STORAGE_KEY); const themeToLoad = savedTheme || 'dark'; if (themeSelector) { const themeExists = [...themeSelector.options].some(option => option.value === themeToLoad); if (themeExists) { themeSelector.value = themeToLoad; } else { console.warn(`Saved theme "${themeToLoad}" not found. Defaulting.`); themeSelector.value = themeSelector.options[0]?.value || 'dark'; localStorage.setItem(THEME_STORAGE_KEY, themeSelector.value); } } else { console.warn("Theme selector element not found on load."); } if (themeStylesheet) { const newHref = `/static/themes/${themeSelector ? themeSelector.value : 'dark'}.css`; themeStylesheet.setAttribute('href', newHref); console.log(`Applied theme stylesheet: ${newHref}`); } else { console.error("Theme stylesheet link element not found on load!"); } }

    // --- AI Model Handling ---
    function handleModelChange(event) { /* ... keep existing ... */ const selectedModel = event.target.value; console.log(`AI Model selected: ${selectedModel}`); currentSelectedModel = selectedModel; localStorage.setItem(MODEL_STORAGE_KEY, selectedModel); }
    function loadSavedModel() { /* ... keep existing ... */ const savedModel = localStorage.getItem(MODEL_STORAGE_KEY); const modelToLoad = savedModel || currentSelectedModel; console.log(`Loading AI Model: ${modelToLoad}`); if (modelSelector) { const modelExists = [...modelSelector.options].some(option => option.value === modelToLoad); if (modelExists) { modelSelector.value = modelToLoad; currentSelectedModel = modelToLoad; } else { console.warn(`Saved model "${modelToLoad}" not found in dropdown. Defaulting.`); currentSelectedModel = modelSelector.options[0]?.value || 'gemini-1.5-flash-latest'; modelSelector.value = currentSelectedModel; localStorage.setItem(MODEL_STORAGE_KEY, currentSelectedModel); } } else { console.warn("Model selector element not found on load."); } console.log(`Current AI Model set to: ${currentSelectedModel}`); }

    // --- Custom Instructions Handling ---
    function handleInstructionsChange(event) { currentSystemInstruction = event.target.value; saveInstructionsToLocalStorage(); console.log("Custom instructions updated (live)."); }
    function saveInstructionsToLocalStorage() { localStorage.setItem(CUSTOM_INSTRUCTIONS_KEY, currentSystemInstruction); console.log("Custom instructions saved to localStorage."); }
    function loadSavedInstructions() { const savedInstructions = localStorage.getItem(CUSTOM_INSTRUCTIONS_KEY); currentSystemInstruction = savedInstructions !== null ? savedInstructions : currentSystemInstruction; if (customInstructionsInput) { customInstructionsInput.value = currentSystemInstruction; } else { console.warn("Custom instructions textarea not found on load."); } console.log(`Loaded system instructions (length: ${currentSystemInstruction.length})`); }

    // --- Copy Code Functionality ---
    function handleCopyCodeClick(event) { const copyButton = event.target.closest('.copy-code-button'); if (!copyButton) return; const codeToCopy = copyButton.dataset.code; if (navigator.clipboard && codeToCopy) { navigator.clipboard.writeText(codeToCopy).then(() => { copyButton.innerHTML = '<i class="fa-solid fa-check"></i> Copied!'; copyButton.classList.add('copied'); setTimeout(() => { copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy'; copyButton.classList.remove('copied'); }, 1500); }).catch(err => { console.error('Failed to copy code: ', err); copyButton.innerHTML = '<i class="fa-solid fa-xmark"></i> Failed'; setTimeout(() => { copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy'; }, 1500); }); } else { console.error('Clipboard API not available or code not found.'); copyButton.innerHTML = '<i class="fa-solid fa-xmark"></i> Error'; setTimeout(() => { copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy'; }, 1500); } }


    // --- Event Handlers ---
    function handleNewChatClick() { /* ... keep existing ... */ closeOpenDropdown('handleNewChatClick'); const newChatId = generateUUID(); const newChat = { id: newChatId, title: "New Chat", timestamp: getTimestamp(), messages: [INITIAL_GREETING_MSG_OBJ] }; allChats.unshift(newChat); saveChatsToLocalStorage(); activateChat(newChatId); }
    function handleSidebarInteraction(event) { /* ... keep existing ... */ const targetElement = event.target; const optionsButton = targetElement.closest('.chat-options-button'); const renameButton = targetElement.closest('.rename-chat-button'); const deleteButton = targetElement.closest('.delete-chat-button'); const clickedInsideOpenDropdown = targetElement.closest('.chat-options-dropdown.show'); const chatItem = targetElement.closest('.chat-list-item:not(.no-chats-placeholder)'); if (optionsButton) { event.stopPropagation(); toggleDropdown(optionsButton.dataset.chatId); return; } if (renameButton) { event.stopPropagation(); handleRenameChat(renameButton.dataset.chatId); return; } if (deleteButton) { event.stopPropagation(); handleDeleteChat(deleteButton.dataset.chatId); return; } if (clickedInsideOpenDropdown) { event.stopPropagation(); return; } closeOpenDropdown('sidebar background'); if (chatItem) { const chatIdToLoad = chatItem.dataset.chatId; if (chatIdToLoad && chatIdToLoad !== currentChatId) { activateChat(chatIdToLoad); } } }
    function handleGlobalClick(event) { /* ... keep existing ... */ if (!openDropdownId) return; const openDropdownElement = document.getElementById(openDropdownId); const listElement = chatList ? chatList.querySelector(`li[data-chat-id="${openDropdownId.replace('dropdown-', '')}"]`) : null; const optionsButtonElement = listElement ? listElement.querySelector('.chat-options-button') : null; if (openDropdownElement && optionsButtonElement && !openDropdownElement.contains(event.target) && !optionsButtonElement.contains(event.target)) { closeOpenDropdown('global click'); } }
    function handleToggleSidebarClick() { /* ... keep existing ... */ closeOpenDropdown('handleToggleSidebarClick'); if (!appContainer || !toggleSidebarButton) return; const isCollapsed = appContainer.classList.toggle('sidebar-collapsed'); toggleSidebarButton.innerHTML = isCollapsed ? '<i class="fa-solid fa-chevron-right"></i>' : '<i class="fa-solid fa-chevron-left"></i>'; }
    function handleChatSettingsClick() { openSettingsPopup(); }
    function handleUserInputKeypress(event) { /* ... keep existing ... */ if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); if (sendButton && !sendButton.disabled) { sendMessage(); } } }


    // --- Initialization ---
    function initializeApp() {
        console.log("Initializing Chat App...");
        loadChatsFromLocalStorage();
        loadSavedTheme(); // Load theme
        loadSavedModel(); // Load model
        loadSavedInstructions(); // *** Load instructions ***

        if (allChats.length > 0) { activateChat(allChats[0].id); }
        else { handleNewChatClick(); }

        // Attach Event Listeners
        if (sendButton) sendButton.addEventListener('click', sendMessage);
        if (userInput) userInput.addEventListener('keypress', handleUserInputKeypress);
        if (newChatButton) newChatButton.addEventListener('click', handleNewChatClick);
        if (chatList) chatList.addEventListener('click', handleSidebarInteraction);
        if (toggleSidebarButton) toggleSidebarButton.addEventListener('click', handleToggleSidebarClick);
        if (settingsButton) settingsButton.addEventListener('click', handleChatSettingsClick);
        document.addEventListener('click', handleGlobalClick);
        // Popup Listeners
        if (closePopupButton) closePopupButton.addEventListener('click', closeSettingsPopup);
        if (popupOverlay) popupOverlay.addEventListener('click', closeSettingsPopup);
        if (themeSelector) themeSelector.addEventListener('change', handleThemeChange);
        if (modelSelector) modelSelector.addEventListener('change', handleModelChange);
        if (customInstructionsInput) customInstructionsInput.addEventListener('input', handleInstructionsChange); // *** Attach instruction change listener ***
        // Copy Code Listener
        if (chatbox) { chatbox.addEventListener('click', handleCopyCodeClick); }

        if (userInput) userInput.focus();
        console.log("Chat App Initialized.");
    }

    // --- Run Initialization ---
    initializeApp();

}); // End DOMContentLoaded
