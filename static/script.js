// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    // --- Selectors ---
    const appContainer = document.getElementById('appContainer');
    const sidebar = document.getElementById('sidebar');
    const chatbox = document.getElementById('chatbox');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    const loadingIndicator = document.getElementById('loading-indicator');
    const toggleSidebarButton = document.getElementById('toggleSidebarButton');
    const newChatButton = document.getElementById('newChatButton');
    const chatList = document.getElementById('chatList');
    // const iconBar = document.getElementById('iconBar'); // Icon bar removed
    const chatHeaderTitle = document.getElementById('chatHeaderTitle');
    // Settings Popup Selectors
    const settingsButton = document.getElementById('chatSettingsButton');
    const popupOverlay = document.getElementById('popupOverlay');
    const settingsPopup = document.getElementById('settingsPopup');
    const closePopupButton = document.getElementById('closePopupButton');
    const themeSelector = document.getElementById('themeSelector');
    const themeStylesheet = document.getElementById('themeStylesheet');
    const modelSelector = document.getElementById('modelSelector');
    const customInstructionsInput = document.getElementById('customInstructionsInput'); // *** Selector for Instructions Textarea ***

    // --- State Variables ---
    let currentChatId = null;
    let allChats = [];
    let openDropdownId = null;
    const LOCAL_STORAGE_KEY = 'zoroChatHistory';
    const THEME_STORAGE_KEY = 'selectedTheme';
    const MODEL_STORAGE_KEY = 'selectedAiModel';
    const CUSTOM_INSTRUCTIONS_KEY = 'customSystemInstructions'; // *** Key for Instructions ***
    let currentSelectedModel = 'gemini-1.5-flash-latest'; // Default model
    // *** Default instructions state variable ***
    let currentSystemInstruction = `You are Zoro, a helpful and respectful personal AI assistant for Blake C.
You should call him 'Sir' and always respond with politeness.`;

    // --- Constants ---
    const INITIAL_GREETING_TEXT = "Greetings, Sir. How may I assist you today?";
    const INITIAL_GREETING_MSG_OBJ = { sender: 'ai', text: INITIAL_GREETING_TEXT, timestamp: Date.now() };
    const CHAT_TITLE_MAX_LENGTH = 28;

    // --- Utility Functions ---
    function generateUUID() { return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c => (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)); }
    function getTimestamp() { return Date.now(); }
    function generateDefaultChatTitle(messageText) { let title = messageText.replace(/^(Sir|Hey|Hello|Hi|Zoro)[,\s]*/i, '').trim(); title = title.charAt(0).toUpperCase() + title.slice(1); if (title.length > CHAT_TITLE_MAX_LENGTH) { title = title.substring(0, CHAT_TITLE_MAX_LENGTH - 3) + '...'; } return title || "New Chat"; }

    // --- LocalStorage Functions ---
    function loadChatsFromLocalStorage() { const storedChats = localStorage.getItem(LOCAL_STORAGE_KEY); try { if (storedChats) { allChats = JSON.parse(storedChats); allChats.sort((a, b) => b.timestamp - a.timestamp); } else { allChats = []; } } catch (error) { console.error("Error parsing chats from localStorage:", error); allChats = []; localStorage.removeItem(LOCAL_STORAGE_KEY); } }
    function saveChatsToLocalStorage() { try { allChats.sort((a, b) => b.timestamp - a.timestamp); localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(allChats)); } catch (error) { console.error("Error saving chats to localStorage:", error); } }

    // --- Configure Marked.js and Highlight.js ---
    marked.setOptions({ highlight: function(code, lang) { const language = hljs.getLanguage(lang) ? lang : 'plaintext'; try { return hljs.highlight(code, { language, ignoreIllegals: true }).value; } catch (error) { console.error("Highlight.js error:", error, "Lang:", lang); return hljs.highlight(code, { language: 'plaintext', ignoreIllegals: true }).value; } }, breaks: true, gfm: true, });

    // --- UI Update Functions ---
    function addMessageToDOM(message) { if (!chatbox) return; const messageDiv = document.createElement('div'); messageDiv.classList.add('message', message.sender === 'user' ? 'user-message' : 'ai-message'); const iconDiv = document.createElement('div'); iconDiv.classList.add('message-icon'); iconDiv.textContent = message.sender === 'user' ? 'Y' : 'Z'; const contentDiv = document.createElement('div'); contentDiv.classList.add('message-content'); const messageText = typeof message.text === 'string' ? message.text : ''; const convertedHtml = marked.parse(messageText); contentDiv.innerHTML = convertedHtml; contentDiv.querySelectorAll('pre code').forEach((codeBlock) => { const preElement = codeBlock.parentElement; if (preElement && preElement.tagName === 'PRE' && !preElement.querySelector('.code-block-header')) { let language = 'plaintext'; const classes = codeBlock.className.split(' '); const langClass = classes.find(cls => cls.startsWith('language-')); if (langClass) { language = langClass.replace('language-', ''); } const headerDiv = document.createElement('div'); headerDiv.className = 'code-block-header'; const langSpan = document.createElement('span'); langSpan.className = 'code-block-language'; langSpan.textContent = language; const copyButton = document.createElement('button'); copyButton.className = 'copy-code-button'; copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy'; copyButton.dataset.code = codeBlock.textContent; headerDiv.appendChild(langSpan); headerDiv.appendChild(copyButton); preElement.insertBefore(headerDiv, codeBlock); } }); if (message.sender === 'user') { messageDiv.appendChild(contentDiv); messageDiv.appendChild(iconDiv); } else { messageDiv.appendChild(iconDiv); messageDiv.appendChild(contentDiv); } chatbox.appendChild(messageDiv); }
    function loadChatMessages(chatId) { const chat = allChats.find(c => c.id === chatId); if (!chatbox) return; chatbox.innerHTML = ''; if (chat && chat.messages) { chat.messages.forEach(addMessageToDOM); if (chatHeaderTitle) chatHeaderTitle.textContent = chat.title || "Chat"; } else { addMessageToDOM(INITIAL_GREETING_MSG_OBJ); if (chatHeaderTitle) chatHeaderTitle.textContent = "Zoro - Personal AI Assistant"; } requestAnimationFrame(() => { if(chatbox) chatbox.scrollTop = chatbox.scrollHeight; }); }
    function updateSidebar() { if (!chatList) return; const fragment = document.createDocumentFragment(); if (allChats.length === 0) { const placeholder = document.createElement('li'); placeholder.className = 'no-chats-placeholder'; placeholder.style.cssText = 'text-align: center; padding: 20px; color: var(--text-medium); font-style: italic; font-size: 0.9em; cursor: default;'; placeholder.textContent = 'No chats yet.'; fragment.appendChild(placeholder); } else { allChats.forEach(chat => { const listItem = document.createElement('li'); listItem.className = 'chat-list-item'; listItem.dataset.chatId = chat.id; const titleSpan = document.createElement('span'); titleSpan.className = 'chat-title'; titleSpan.textContent = chat.title || 'Chat'; listItem.appendChild(titleSpan); const optionsButton = document.createElement('button'); optionsButton.className = 'chat-options-button'; optionsButton.innerHTML = '<i class="fa-solid fa-ellipsis"></i>'; optionsButton.dataset.chatId = chat.id; listItem.appendChild(optionsButton); const dropdown = document.createElement('div'); dropdown.className = 'chat-options-dropdown'; dropdown.id = `dropdown-${chat.id}`; const renameButton = document.createElement('button'); renameButton.className = 'rename-chat-button'; renameButton.dataset.chatId = chat.id; renameButton.innerHTML = '<i class="fa-solid fa-pencil"></i> Rename'; dropdown.appendChild(renameButton); const deleteButton = document.createElement('button'); deleteButton.className = 'delete-chat-button'; deleteButton.dataset.chatId = chat.id; deleteButton.innerHTML = '<i class="fa-solid fa-trash-can"></i> Delete'; dropdown.appendChild(deleteButton); listItem.appendChild(dropdown); if (chat.id === currentChatId) { listItem.classList.add('active-chat'); } fragment.appendChild(listItem); }); } chatList.innerHTML = ''; chatList.appendChild(fragment); }
    function activateChat(chatId) { if (!chatId) return; closeOpenDropdown('activateChat'); currentChatId = chatId; loadChatMessages(chatId); updateSidebar(); if (userInput) userInput.focus(); }
    function showLoading(isLoading) { if (userInput) userInput.disabled = isLoading; if (sendButton) { sendButton.disabled = isLoading; sendButton.innerHTML = isLoading ? '<i class="fa-solid fa-spinner fa-spin"></i>' : '<i class="fa-solid fa-paper-plane"></i>'; } }

    // --- Dropdown Functions ---
    function closeOpenDropdown(debugSource = "unknown") { if (openDropdownId) { const dropdown = document.getElementById(openDropdownId); if (dropdown) { dropdown.classList.remove('show'); } openDropdownId = null; } }
    function toggleDropdown(chatId) { const dropdownId = `dropdown-${chatId}`; const dropdown = document.getElementById(dropdownId); if (!dropdown) { console.error(`!! Dropdown element not found: ${dropdownId}`); return; } const currentlyOpen = dropdown.classList.contains('show'); const wasOpenId = openDropdownId; closeOpenDropdown('toggleDropdown'); if (!currentlyOpen || wasOpenId !== dropdownId) { if (wasOpenId !== dropdownId) { dropdown.classList.add('show'); openDropdownId = dropdownId; /* console.log(`>>> Opened dropdown: ${dropdownId}`); */ } } }

    // --- Rename/Delete Logic ---
    function handleRenameChat(chatId) { const chatIndex = allChats.findIndex(c => c.id === chatId); if (chatIndex === -1) return; const oldTitle = allChats[chatIndex].title; const newTitle = prompt("Enter new chat name:", oldTitle || ""); if (newTitle !== null && newTitle.trim() !== "" && newTitle !== oldTitle) { allChats[chatIndex].title = newTitle.trim(); allChats[chatIndex].timestamp = getTimestamp(); saveChatsToLocalStorage(); updateSidebar(); if (currentChatId === chatId && chatHeaderTitle) chatHeaderTitle.textContent = allChats[chatIndex].title; console.log(`Chat ${chatId} renamed to "${newTitle}"`); } closeOpenDropdown('handleRenameChat'); }
    function handleDeleteChat(chatId) { const chatIndex = allChats.findIndex(c => c.id === chatId); if (chatIndex === -1) return; const chatTitle = allChats[chatIndex].title || "this chat"; if (confirm(`Are you sure you want to delete "${chatTitle}"? This cannot be undone.`)) { allChats.splice(chatIndex, 1); saveChatsToLocalStorage(); console.log(`Chat ${chatId} deleted`); if (currentChatId === chatId) { currentChatId = null; if (allChats.length > 0) { activateChat(allChats[0].id); } else { handleNewChatClick(); } } else { updateSidebar(); } } closeOpenDropdown('handleDeleteChat'); }

    // --- AI Title Generation ---
    async function fetchAndSetAiTitle(chatId, userMessageText, aiResponseText) { console.log(`Attempting to generate AI title for chat: ${chatId} using model: ${currentSelectedModel}`); let needsDefaultFallback = false; if (!userMessageText || !aiResponseText || aiResponseText.includes("apologize") || aiResponseText.includes("error")) { console.warn("Skipping AI title generation due to potentially empty/error initial messages."); needsDefaultFallback = true; } if (!needsDefaultFallback) { try { const response = await fetch('/generate-title', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ user_message: userMessageText, ai_response: aiResponseText, model_name: currentSelectedModel }), }); if (!response.ok) { console.error(`Error fetching title (${response.status}): ${response.statusText}`); needsDefaultFallback = true; } else { const data = await response.json(); if (data && data.title) { const generatedTitle = data.title; console.log(`Received AI title: "${generatedTitle}" for chat ${chatId}`); const chatIndex = allChats.findIndex(c => c.id === chatId); if (chatIndex !== -1) { if (allChats[chatIndex].title !== generatedTitle) { allChats[chatIndex].title = generatedTitle; saveChatsToLocalStorage(); updateSidebar(); if (currentChatId === chatId && chatHeaderTitle) chatHeaderTitle.textContent = generatedTitle; } return; } else { console.warn(`Chat ${chatId} not found when setting AI title.`); } } else { console.warn("AI title generation returned no title.", data); needsDefaultFallback = true; } } } catch (error) { console.error("Network error during AI title generation:", error); needsDefaultFallback = true; } } if (needsDefaultFallback) { const chatIndex = allChats.findIndex(c => c.id === chatId); if (chatIndex !== -1 && allChats[chatIndex].title === "New Chat") { const defaultTitle = generateDefaultChatTitle(userMessageText); if (allChats[chatIndex].title !== defaultTitle) { allChats[chatIndex].title = defaultTitle; saveChatsToLocalStorage(); updateSidebar(); if (currentChatId === chatId && chatHeaderTitle) chatHeaderTitle.textContent = defaultTitle; console.log(`Used default title: "${defaultTitle}"`); } } } }

    // --- Main Chat Functionality ---
    async function sendMessage() {
        if (!userInput || !currentChatId) return;
        const messageText = userInput.value.trim();
        if (!messageText) return;
        console.log(`Sending message using model: ${currentSelectedModel}`);
        // Send current instruction text
        console.log(`Using instructions (length: ${currentSystemInstruction.length})`);
        const userMessage = { sender: 'user', text: messageText, timestamp: getTimestamp() };
        addMessageToDOM(userMessage);
        userInput.value = '';
        showLoading(true);
        if (chatbox) requestAnimationFrame(() => { chatbox.scrollTop = chatbox.scrollHeight; });
        const currentChatIndex = allChats.findIndex(c => c.id === currentChatId);
        if (currentChatIndex === -1) { console.error("Critical: Current chat not found!"); showLoading(false); return; }
        const isFirstUserExchange = allChats[currentChatIndex].messages.length === 1;
        allChats[currentChatIndex].messages.push(userMessage);
        allChats[currentChatIndex].timestamp = getTimestamp();
        saveChatsToLocalStorage();
        let aiResponseText = null;
        try { // Get AI Response
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: messageText,
                    model_name: currentSelectedModel,
                    system_instruction: currentSystemInstruction // *** SEND INSTRUCTIONS ***
                 }),
            });
            let responseData = null;
            if (!response.ok) { aiResponseText = `Sir, there was a server error (Status: ${response.status}). Please try again later.`; try { responseData = await response.json(); if (responseData && responseData.error) aiResponseText = `Sir, an error occurred: ${responseData.error}`; } catch (e) {} console.error('Error fetching AI response:', response.statusText);
            } else { responseData = await response.json(); if (responseData.error) { aiResponseText = `Sir, I encountered an issue: ${responseData.error}`; console.error('Backend error:', responseData.error); } else if (responseData.response) { aiResponseText = responseData.response; } else { aiResponseText = "Sir, I received an empty response. Could you please clarify?"; console.warn("Received OK status but no response data."); } }
            const aiMessage = { sender: 'ai', text: aiResponseText || "Error receiving response.", timestamp: getTimestamp() };
            addMessageToDOM(aiMessage);
            if (chatbox) requestAnimationFrame(() => { chatbox.scrollTop = chatbox.scrollHeight; });
            const updatedChatIndex = allChats.findIndex(c => c.id === currentChatId);
            if (updatedChatIndex !== -1) {
                 let validAiResponse = aiResponseText && !aiResponseText.startsWith("Sir, I apologize") && !aiResponseText.startsWith("Sir, I encountered") && !aiResponseText.includes("Error receiving response");
                 if (validAiResponse) { allChats[updatedChatIndex].messages.push(aiMessage); allChats[updatedChatIndex].timestamp = getTimestamp(); saveChatsToLocalStorage(); if (isFirstUserExchange) { fetchAndSetAiTitle(currentChatId, messageText, aiResponseText); } }
                 else { console.log("Skipping saving AI error/empty message to history."); }
                 updateSidebar();
            } else { console.error("Critical: Current chat lost after AI response!"); }
        } catch (error) { // Handle Network Error
            const errorMsg = 'Sir, I seem to be unable to connect. Please check the network connection and try again.';
            addMessageToDOM({ sender: 'ai', text: errorMsg, timestamp: getTimestamp() });
            if (chatbox) requestAnimationFrame(() => { chatbox.scrollTop = chatbox.scrollHeight; });
            console.error('Network error during chat fetch:', error);
            updateSidebar();
        } finally { showLoading(false); }
    }

    // --- Popup Handling Functions ---
    function openSettingsPopup() { closeOpenDropdown('openSettingsPopup'); if (popupOverlay && settingsPopup) { popupOverlay.classList.add('show'); settingsPopup.classList.add('show'); } else { console.error("Popup overlay or settings popup element not found!"); } }
    function closeSettingsPopup() { if (popupOverlay && settingsPopup) { popupOverlay.classList.remove('show'); settingsPopup.classList.remove('show'); } }

    // --- Theme Handling ---
    function handleThemeChange(event) { const selectedTheme = event.target.value; if (themeStylesheet) { const newHref = `/static/themes/${selectedTheme}.css`; themeStylesheet.setAttribute('href', newHref); localStorage.setItem(THEME_STORAGE_KEY, selectedTheme); console.log(`Theme stylesheet changed to: ${newHref}`); } else { console.error("Theme stylesheet link element not found!"); } }
    function loadSavedTheme() { const savedTheme = localStorage.getItem(THEME_STORAGE_KEY); const themeToLoad = savedTheme || 'dark'; if (themeSelector) { const themeExists = [...themeSelector.options].some(option => option.value === themeToLoad); if (themeExists) { themeSelector.value = themeToLoad; } else { console.warn(`Saved theme "${themeToLoad}" not found. Defaulting.`); themeSelector.value = themeSelector.options[0]?.value || 'dark'; localStorage.setItem(THEME_STORAGE_KEY, themeSelector.value); } } else { console.warn("Theme selector element not found on load."); } if (themeStylesheet) { const newHref = `/static/themes/${themeSelector ? themeSelector.value : 'dark'}.css`; themeStylesheet.setAttribute('href', newHref); console.log(`Applied theme stylesheet: ${newHref}`); } else { console.error("Theme stylesheet link element not found on load!"); } }

    // --- AI Model Handling ---
    function handleModelChange(event) { const selectedModel = event.target.value; console.log(`AI Model selected: ${selectedModel}`); currentSelectedModel = selectedModel; localStorage.setItem(MODEL_STORAGE_KEY, selectedModel); }
    function loadSavedModel() { const savedModel = localStorage.getItem(MODEL_STORAGE_KEY); const modelToLoad = savedModel || currentSelectedModel; console.log(`Loading AI Model: ${modelToLoad}`); if (modelSelector) { const modelExists = [...modelSelector.options].some(option => option.value === modelToLoad); if (modelExists) { modelSelector.value = modelToLoad; currentSelectedModel = modelToLoad; } else { console.warn(`Saved model "${modelToLoad}" not found in dropdown. Defaulting.`); currentSelectedModel = modelSelector.options[0]?.value || 'gemini-1.5-flash-latest'; modelSelector.value = currentSelectedModel; localStorage.setItem(MODEL_STORAGE_KEY, currentSelectedModel); } } else { console.warn("Model selector element not found on load."); } console.log(`Current AI Model set to: ${currentSelectedModel}`); }

    // --- Copy Code Functionality ---
    function handleCopyCodeClick(event) { const copyButton = event.target.closest('.copy-code-button'); if (!copyButton) return; const codeToCopy = copyButton.dataset.code; if (navigator.clipboard && codeToCopy) { navigator.clipboard.writeText(codeToCopy).then(() => { copyButton.innerHTML = '<i class="fa-solid fa-check"></i> Copied!'; copyButton.classList.add('copied'); setTimeout(() => { copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy'; copyButton.classList.remove('copied'); }, 1500); }).catch(err => { console.error('Failed to copy code: ', err); copyButton.innerHTML = '<i class="fa-solid fa-xmark"></i> Failed'; setTimeout(() => { copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy'; }, 1500); }); } else { console.error('Clipboard API not available or code not found.'); copyButton.innerHTML = '<i class="fa-solid fa-xmark"></i> Error'; setTimeout(() => { copyButton.innerHTML = '<i class="fa-regular fa-copy"></i> Copy'; }, 1500); } }

    // *** NEW: Custom Instructions Handling ***
    function handleInstructionsChange(event) {
        currentSystemInstruction = event.target.value;
        saveInstructionsToLocalStorage(); // Save on change (input event)
        console.log("Custom instructions updated (live).");
    }

    function saveInstructionsToLocalStorage() {
         localStorage.setItem(CUSTOM_INSTRUCTIONS_KEY, currentSystemInstruction);
         console.log("Custom instructions saved to localStorage.");
    }

    function loadSavedInstructions() {
        const savedInstructions = localStorage.getItem(CUSTOM_INSTRUCTIONS_KEY);
        // Use saved value OR the initial default defined in the state variables
        currentSystemInstruction = savedInstructions !== null ? savedInstructions : currentSystemInstruction; // Keep default if nothing saved

        if (customInstructionsInput) {
            customInstructionsInput.value = currentSystemInstruction; // Populate textarea
        } else {
            console.warn("Custom instructions textarea not found on load.");
        }
        console.log(`Loaded system instructions (length: ${currentSystemInstruction.length})`);
    }
    // *** END OF NEW Custom Instructions Handling ***


    // --- Event Handlers ---
    function handleNewChatClick() { closeOpenDropdown('handleNewChatClick'); const newChatId = generateUUID(); const newChat = { id: newChatId, title: "New Chat", timestamp: getTimestamp(), messages: [INITIAL_GREETING_MSG_OBJ] }; allChats.unshift(newChat); saveChatsToLocalStorage(); activateChat(newChatId); }
    function handleSidebarInteraction(event) { const targetElement = event.target; const optionsButton = targetElement.closest('.chat-options-button'); const renameButton = targetElement.closest('.rename-chat-button'); const deleteButton = targetElement.closest('.delete-chat-button'); const clickedInsideOpenDropdown = targetElement.closest('.chat-options-dropdown.show'); const chatItem = targetElement.closest('.chat-list-item:not(.no-chats-placeholder)'); if (optionsButton) { event.stopPropagation(); toggleDropdown(optionsButton.dataset.chatId); return; } if (renameButton) { event.stopPropagation(); handleRenameChat(renameButton.dataset.chatId); return; } if (deleteButton) { event.stopPropagation(); handleDeleteChat(deleteButton.dataset.chatId); return; } if (clickedInsideOpenDropdown) { event.stopPropagation(); return; } closeOpenDropdown('sidebar background'); if (chatItem) { const chatIdToLoad = chatItem.dataset.chatId; if (chatIdToLoad && chatIdToLoad !== currentChatId) { activateChat(chatIdToLoad); } } }
    function handleGlobalClick(event) { if (!openDropdownId) return; const openDropdownElement = document.getElementById(openDropdownId); const listElement = chatList ? chatList.querySelector(`li[data-chat-id="${openDropdownId.replace('dropdown-', '')}"]`) : null; const optionsButtonElement = listElement ? listElement.querySelector('.chat-options-button') : null; if (openDropdownElement && optionsButtonElement && !openDropdownElement.contains(event.target) && !optionsButtonElement.contains(event.target)) { closeOpenDropdown('global click'); } }
    function handleToggleSidebarClick() { closeOpenDropdown('handleToggleSidebarClick'); if (!appContainer || !toggleSidebarButton) return; const isCollapsed = appContainer.classList.toggle('sidebar-collapsed'); toggleSidebarButton.innerHTML = isCollapsed ? '<i class="fa-solid fa-chevron-right"></i>' : '<i class="fa-solid fa-chevron-left"></i>'; }
    // function handleIconBarClick(event) { /* Icon bar removed */ }
    function handleChatSettingsClick() { openSettingsPopup(); }
    function handleUserInputKeypress(event) { if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); if (sendButton && !sendButton.disabled) { sendMessage(); } } }


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
        // if (iconBar) iconBar.addEventListener('click', handleIconBarClick); // Icon bar removed
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