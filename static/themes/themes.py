import os

# Define the base directory for static files and the themes sub-directory
static_dir = "static"
themes_dir = os.path.join(static_dir, "themes")

# --- Define Color Palettes for Each Theme ---
# Added some common accent colors where appropriate for syntax highlighting
# These might need tweaking for perfect visual harmony per theme
themes = {
    "dark": {
        # ... (Existing dark variables) ...
        "--bg-darkest": "#202123", "--bg-darker": "#343541", "--bg-dark-accent": "#40414f", "--bg-light-accent": "#444654",
        "--text-light": "#ececf1", "--text-medium": "#d1d5db", "--text-dark": "#343541",
        "--user-message-bg": "#10a37f", "--button-primary-bg": "#10a37f", "--button-primary-hover-bg": "#048365",
        "--border-color": "#565869", "--icon-active-bg": "#c52d2d", "--sidebar-hover-bg": "#4d4f5c",
        "--new-chat-bg": "#05a07c", "--new-chat-hover-bg": "#048365", "--scrollbar-thumb-bg": "#444654",
        "--scrollbar-track-bg": "#343541", "--placeholder-text": "#8e8ea0", "--dropdown-bg": "#505261",
        "--delete-color": "#f87171", "--delete-hover-bg": "#dc2626", "--popup-bg": "#40414f",
        "--popup-text": "#ececf1", "--overlay-bg": "rgba(0, 0, 0, 0.6)", "--input-bg": "#444654",
        "--input-border": "#565869", "--input-text": "#ececf1",
        # Markdown Specific
        "--code-header-bg": "rgba(255, 255, 255, 0.08)", "--code-bg": "rgba(0, 0, 0, 0.3)",
        "--inline-code-bg": "rgba(255, 255, 255, 0.1)", "--inline-code-text": "var(--text-light)",
        "--blockquote-border": "var(--user-message-bg)", "--blockquote-text": "var(--text-medium)",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        # Syntax Highlighting (Dark) - Using existing vars where possible
        "--syntax-keyword": "#c792ea", # Purpleish (Example)
        "--syntax-string": "#c3e88d", # Greenish (Example)
        "--syntax-comment": "#546e7a", # Greyish blue (Example)
        "--syntax-number": "#f78c6c", # Orangeish (Example)
        "--syntax-function": "#82aaff", # Blueish (Example)
        "--syntax-class": "#ffcb6b", # Yellowish (Example)
        "--syntax-tag": "#f07178", # Reddish (Example)
        "--syntax-attr": "#ffcb6b", # Yellowish (Example)
        "--syntax-literal": "#82aaff" # Blueish (Example)
    },
    "light": {
        # ... (Existing light variables) ...
        "--bg-darkest": "#e0e0e0", "--bg-darker": "#f4f4f5", "--bg-dark-accent": "#ffffff", "--bg-light-accent": "#e5e7eb",
        "--text-light": "#1f2937", "--text-medium": "#4b5563", "--text-dark": "#111827",
        "--user-message-bg": "#059669", "--button-primary-bg": "#059669", "--button-primary-hover-bg": "#047857",
        "--border-color": "#d1d5db", "--icon-active-bg": "#dc2626", "--sidebar-hover-bg": "#f3f4f6",
        "--new-chat-bg": "#059669", "--new-chat-hover-bg": "#047857", "--scrollbar-thumb-bg": "#c7cdd6",
        "--scrollbar-track-bg": "#f4f4f5", "--placeholder-text": "#9ca3af", "--dropdown-bg": "#ffffff",
        "--delete-color": "#dc2626", "--delete-hover-bg": "#ef4444", "--popup-bg": "#ffffff",
        "--popup-text": "#1f2937", "--overlay-bg": "rgba(100, 116, 139, 0.4)", "--input-bg": "#ffffff",
        "--input-border": "#d1d5db", "--input-text": "#1f2937",
        # Markdown Specific
        "--code-header-bg": "rgba(0, 0, 0, 0.03)", "--code-bg": "rgba(0, 0, 0, 0.05)",
        "--inline-code-bg": "rgba(0, 0, 0, 0.08)", "--inline-code-text": "var(--text-light)",
        "--blockquote-border": "var(--user-message-bg)", "--blockquote-text": "var(--text-medium)",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-dark)",
         # Syntax Highlighting (Light) - Need darker colors
        "--syntax-keyword": "#7c4dff", # Dark Purple
        "--syntax-string": "#43a047", # Dark Green
        "--syntax-comment": "#6a737d", # Dark Grey
        "--syntax-number": "#d32f2f", # Dark Red/Orange
        "--syntax-function": "#0277bd", # Dark Blue
        "--syntax-class": "#f57f17", # Dark Yellow/Orange
        "--syntax-tag": "#d32f2f", # Dark Red
        "--syntax-attr": "#f57f17", # Dark Yellow/Orange
        "--syntax-literal": "#0277bd" # Dark Blue
    },
    # --- Add similar "--syntax-..." variables to ALL other theme palettes ---
    # Example for Dracula (copy & paste, then adjust colors)
    "dracula": {
        "--bg-darkest": "#21222c", "--bg-darker": "#282a36", "--bg-dark-accent": "#3a3c4e", "--bg-light-accent": "#44475a",
        "--text-light": "#f8f8f2", "--text-medium": "#bd93f9", "--text-dark": "#282a36",
        "--user-message-bg": "#50fa7b", "--button-primary-bg": "#bd93f9", "--button-primary-hover-bg": "#9a7ecc",
        "--border-color": "#6272a4", "--icon-bar-bg": "#191a21", "--icon-active-bg": "#ff5555",
        "--sidebar-hover-bg": "#44475a", "--new-chat-bg": "#8be9fd", "--new-chat-hover-bg": "#6cdcf0",
        "--scrollbar-thumb-bg": "#6272a4", "--scrollbar-track-bg": "#282a36", "--placeholder-text": "#6272a4",
        "--dropdown-bg": "#3a3c4e", "--delete-color": "#ff5555", "--delete-hover-bg": "#ff7979",
        "--popup-bg": "#3a3c4e", "--popup-text": "#f8f8f2", "--overlay-bg": "rgba(0, 0, 0, 0.6)",
        "--input-bg": "#44475a", "--input-border": "#6272a4", "--input-text": "#f8f8f2",
        "--code-header-bg": "#44475a", "--code-bg": "#21222c", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#ff79c6", "--blockquote-border": "#ffb86c", "--blockquote-text": "#f1fa8c",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        # Syntax Highlighting (Dracula)
        "--syntax-keyword": "#ff79c6", # Pink
        "--syntax-string": "#f1fa8c", # Yellow
        "--syntax-comment": "#6272a4", # Grey/Blue
        "--syntax-number": "#bd93f9", # Purple
        "--syntax-function": "#50fa7b", # Green
        "--syntax-class": "#8be9fd", # Cyan
        "--syntax-tag": "#ff79c6", # Pink
        "--syntax-attr": "#50fa7b", # Green
        "--syntax-literal": "#bd93f9" # Purple
    },
    # --- Repeat for ALL other themes (monokai, nord, gruvbox, etc.) ---
    # ... (You'll need to define appropriate --syntax-* colors for each) ...
    # (For brevity, I'm omitting the rest, but the pattern is the same)
    "monokai": {
        "--bg-darkest": "#222222", "--bg-darker": "#272822", "--bg-dark-accent": "#3d3e3a", "--bg-light-accent": "#49483e",
        "--text-light": "#f8f8f2", "--text-medium": "#a6e22e", "--text-dark": "#272822",
        "--user-message-bg": "#66d9ef", "--button-primary-bg": "#f92672", "--button-primary-hover-bg": "#e01d63",
        "--border-color": "#75715e", "--icon-bar-bg": "#1b1c18", "--icon-active-bg": "#f92672",
        "--sidebar-hover-bg": "#49483e", "--new-chat-bg": "#a6e22e", "--new-chat-hover-bg": "#8bc41e",
        "--scrollbar-thumb-bg": "#75715e", "--scrollbar-track-bg": "#272822", "--placeholder-text": "#75715e",
        "--dropdown-bg": "#3d3e3a", "--delete-color": "#f92672", "--delete-hover-bg": "#fd5ff1",
        "--popup-bg": "#3d3e3a", "--popup-text": "#f8f8f2", "--overlay-bg": "rgba(0, 0, 0, 0.7)",
        "--input-bg": "#49483e", "--input-border": "#75715e", "--input-text": "#f8f8f2",
        "--code-header-bg": "#49483e", "--code-bg": "#222222", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#fd971f", "--blockquote-border": "#ae81ff", "--blockquote-text": "#e6db74",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        "--syntax-keyword": "#f92672", "--syntax-string": "#e6db74", "--syntax-comment": "#75715e",
        "--syntax-number": "#ae81ff", "--syntax-function": "#a6e22e", "--syntax-class": "#66d9ef",
        "--syntax-tag": "#f92672", "--syntax-attr": "#a6e22e", "--syntax-literal": "#ae81ff"
    },
     "nord": {
        "--bg-darkest": "#242933", "--bg-darker": "#2e3440", "--bg-dark-accent": "#3b4252", "--bg-light-accent": "#434c5e",
        "--text-light": "#eceff4", "--text-medium": "#d8dee9", "--text-dark": "#2e3440",
        "--user-message-bg": "#a3be8c", "--button-primary-bg": "#88c0d0", "--button-primary-hover-bg": "#6caebb",
        "--border-color": "#4c566a", "--icon-bar-bg": "#242933", "--icon-active-bg": "#bf616a",
        "--sidebar-hover-bg": "#434c5e", "--new-chat-bg": "#81a1c1", "--new-chat-hover-bg": "#698aac",
        "--scrollbar-thumb-bg": "#4c566a", "--scrollbar-track-bg": "#2e3440", "--placeholder-text": "#4c566a",
        "--dropdown-bg": "#3b4252", "--delete-color": "#bf616a", "--delete-hover-bg": "#d08770",
        "--popup-bg": "#3b4252", "--popup-text": "#eceff4", "--overlay-bg": "rgba(46, 52, 64, 0.7)",
        "--input-bg": "#434c5e", "--input-border": "#4c566a", "--input-text": "#eceff4",
        "--code-header-bg": "#434c5e", "--code-bg": "#292e39", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#b48ead", "--blockquote-border": "#8fbcbb", "--blockquote-text": "#a3be8c",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        "--syntax-keyword": "#81a1c1", "--syntax-string": "#a3be8c", "--syntax-comment": "#4c566a",
        "--syntax-number": "#b48ead", "--syntax-function": "#88c0d0", "--syntax-class": "#8fbcbb",
        "--syntax-tag": "#81a1c1", "--syntax-attr": "#8fbcbb", "--syntax-literal": "#b48ead"
    },
    "gruvbox-dark": {
        "--bg-darkest": "#1d2021", "--bg-darker": "#282828", "--bg-dark-accent": "#3c3836", "--bg-light-accent": "#504945",
        "--text-light": "#ebdbb2", "--text-medium": "#d5c4a1", "--text-dark": "#282828",
        "--user-message-bg": "#98971a", "--button-primary-bg": "#458588", "--button-primary-hover-bg": "#076678",
        "--border-color": "#665c54", "--icon-bar-bg": "#1d2021", "--icon-active-bg": "#cc241d",
        "--sidebar-hover-bg": "#504945", "--new-chat-bg": "#689d6a", "--new-chat-hover-bg": "#427b58",
        "--scrollbar-thumb-bg": "#665c54", "--scrollbar-track-bg": "#282828", "--placeholder-text": "#7c6f64",
        "--dropdown-bg": "#3c3836", "--delete-color": "#cc241d", "--delete-hover-bg": "#fb4934",
        "--popup-bg": "#3c3836", "--popup-text": "#ebdbb2", "--overlay-bg": "rgba(40, 40, 40, 0.7)",
        "--input-bg": "#504945", "--input-border": "#665c54", "--input-text": "#ebdbb2",
        "--code-header-bg": "#504945", "--code-bg": "#1d2021", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#fe8019", "--blockquote-border": "#d79921", "--blockquote-text": "#bdae93",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        "--syntax-keyword": "#fb4934", "--syntax-string": "#b8bb26", "--syntax-comment": "#928374",
        "--syntax-number": "#d3869b", "--syntax-function": "#8ec07c", "--syntax-class": "#fabd2f",
        "--syntax-tag": "#fb4934", "--syntax-attr": "#8ec07c", "--syntax-literal": "#d3869b"
    },
    "solarized-dark": {
        "--bg-darkest": "#00212b", "--bg-darker": "#002b36", "--bg-dark-accent": "#073642", "--bg-light-accent": "#586e75",
        "--text-light": "#93a1a1", "--text-medium": "#839496", "--text-dark": "#002b36",
        "--user-message-bg": "#859900", "--button-primary-bg": "#268bd2", "--button-primary-hover-bg": "#1a679a",
        "--border-color": "#657b83", "--icon-bar-bg": "#00212b", "--icon-active-bg": "#dc322f",
        "--sidebar-hover-bg": "#073642", "--new-chat-bg": "#2aa198", "--new-chat-hover-bg": "#1c877e",
        "--scrollbar-thumb-bg": "#657b83", "--scrollbar-track-bg": "#002b36", "--placeholder-text": "#586e75",
        "--dropdown-bg": "#073642", "--delete-color": "#dc322f", "--delete-hover-bg": "#cb4b16",
        "--popup-bg": "#073642", "--popup-text": "#93a1a1", "--overlay-bg": "rgba(0, 43, 54, 0.7)",
        "--input-bg": "#073642", "--input-border": "#586e75", "--input-text": "#93a1a1",
        "--code-header-bg": "#586e75", "--code-bg": "#00212b", "--inline-code-bg": "var(--bg-dark-accent)",
        "--inline-code-text": "#b58900", "--blockquote-border": "#d33682", "--blockquote-text": "#6c71c4",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-medium)",
        "--syntax-keyword": "#859900", "--syntax-string": "#2aa198", "--syntax-comment": "#586e75",
        "--syntax-number": "#d33682", "--syntax-function": "#268bd2", "--syntax-class": "#b58900",
        "--syntax-tag": "#859900", "--syntax-attr": "#93a1a1", "--syntax-literal": "#d33682"
    },
    "solarized-light": {
        "--bg-darkest": "#e4e4e4", "--bg-darker": "#fdf6e3", "--bg-dark-accent": "#eee8d5", "--bg-light-accent": "#e9e2c9",
        "--text-light": "#586e75", "--text-medium": "#657b83", "--text-dark": "#002b36",
        "--user-message-bg": "#859900", "--button-primary-bg": "#268bd2", "--button-primary-hover-bg": "#1a679a",
        "--border-color": "#d5cdba", "--icon-bar-bg": "#eee8d5", "--icon-active-bg": "#dc322f",
        "--sidebar-hover-bg": "#e9e2c9", "--new-chat-bg": "#2aa198", "--new-chat-hover-bg": "#1c877e",
        "--scrollbar-thumb-bg": "#b0aca0", "--scrollbar-track-bg": "#fdf6e3", "--placeholder-text": "#93a1a1",
        "--dropdown-bg": "#eee8d5", "--delete-color": "#dc322f", "--delete-hover-bg": "#cb4b16",
        "--popup-bg": "#eee8d5", "--popup-text": "#586e75", "--overlay-bg": "rgba(101, 123, 131, 0.4)",
        "--input-bg": "#eee8d5", "--input-border": "#d5cdba", "--input-text": "#586e75",
        "--code-header-bg": "#e9e2c9", "--code-bg": "#f8f1db", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#b58900", "--blockquote-border": "#d33682", "--blockquote-text": "#6c71c4",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-dark)",
        "--syntax-keyword": "#859900", "--syntax-string": "#2aa198", "--syntax-comment": "#93a1a1",
        "--syntax-number": "#d33682", "--syntax-function": "#268bd2", "--syntax-class": "#b58900",
        "--syntax-tag": "#859900", "--syntax-attr": "#657b83", "--syntax-literal": "#d33682"
    },
    "ocean": {
        "--bg-darkest": "#1a2b34", "--bg-darker": "#2b3e50", "--bg-dark-accent": "#34495e", "--bg-light-accent": "#4f6a7f",
        "--text-light": "#c0c5ce", "--text-medium": "#a3b1c2", "--text-dark": "#2b3e50",
        "--user-message-bg": "#90ee90", "--button-primary-bg": "#5fa8ee", "--button-primary-hover-bg": "#3c8fda",
        "--border-color": "#6a7f94", "--icon-bar-bg": "#1a2b34", "--icon-active-bg": "#e67e22",
        "--sidebar-hover-bg": "#4f6a7f", "--new-chat-bg": "#1abc9c", "--new-chat-hover-bg": "#16a085",
        "--scrollbar-thumb-bg": "#6a7f94", "--scrollbar-track-bg": "#2b3e50", "--placeholder-text": "#6a7f94",
        "--dropdown-bg": "#34495e", "--delete-color": "#e74c3c", "--delete-hover-bg": "#c0392b",
        "--popup-bg": "#34495e", "--popup-text": "#c0c5ce", "--overlay-bg": "rgba(43, 62, 80, 0.7)",
        "--input-bg": "#4f6a7f", "--input-border": "#6a7f94", "--input-text": "#c0c5ce",
        "--code-header-bg": "#4f6a7f", "--code-bg": "#223344", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#fac863", "--blockquote-border": "#c397d8", "--blockquote-text": "#b8c1ce",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        "--syntax-keyword": "#c397d8", "--syntax-string": "#90ee90", "--syntax-comment": "#6a7f94",
        "--syntax-number": "#f99157", "--syntax-function": "#5fa8ee", "--syntax-class": "#fac863",
        "--syntax-tag": "#e74c3c", "--syntax-attr": "#90ee90", "--syntax-literal": "#f99157"
    },
     "sky": {
        "--bg-darkest": "#d4eaf7", "--bg-darker": "#e9f5ff", "--bg-dark-accent": "#ffffff", "--bg-light-accent": "#d0e8f8",
        "--text-light": "#3a506b", "--text-medium": "#5c7da0", "--text-dark": "#1c2e42",
        "--user-message-bg": "#87ceeb", "--button-primary-bg": "#5bbfd3", "--button-primary-hover-bg": "#40a8be",
        "--border-color": "#b8d8ee", "--icon-bar-bg": "#cce4f2", "--icon-active-bg": "#ff6f61",
        "--sidebar-hover-bg": "#e0f0fa", "--new-chat-bg": "#6cb4d8", "--new-chat-hover-bg": "#539cc6",
        "--scrollbar-thumb-bg": "#a8c9e0", "--scrollbar-track-bg": "#e9f5ff", "--placeholder-text": "#8fa7bf",
        "--dropdown-bg": "#ffffff", "--delete-color": "#ff6f61", "--delete-hover-bg": "#f74f4f",
        "--popup-bg": "#ffffff", "--popup-text": "#3a506b", "--overlay-bg": "rgba(176, 206, 230, 0.5)",
        "--input-bg": "#ffffff", "--input-border": "#b8d8ee", "--input-text": "#3a506b",
        "--code-header-bg": "#d0e8f8", "--code-bg": "#f0f8ff", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#4a6d8b", "--blockquote-border": "#77b3d4", "--blockquote-text": "#6e8ca5",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-dark)",
        "--syntax-keyword": "#539cc6", "--syntax-string": "#7fb685", "--syntax-comment": "#99aabb",
        "--syntax-number": "#d88373", "--syntax-function": "#5bbfd3", "--syntax-class": "#40a8be",
        "--syntax-tag": "#ff6f61", "--syntax-attr": "#7fb685", "--syntax-literal": "#d88373"
    },
    "forest": {
        "--bg-darkest": "#2a3d2a", "--bg-darker": "#3d553d", "--bg-dark-accent": "#4a6d4a", "--bg-light-accent": "#6b8e6b",
        "--text-light": "#e0e0d1", "--text-medium": "#b8c4b8", "--text-dark": "#2a3d2a",
        "--user-message-bg": "#a3b86c", "--button-primary-bg": "#8fbc8f", "--button-primary-hover-bg": "#7aa97a",
        "--border-color": "#7f9f7f", "--icon-bar-bg": "#2a3d2a", "--icon-active-bg": "#d2691e",
        "--sidebar-hover-bg": "#6b8e6b", "--new-chat-bg": "#556b2f", "--new-chat-hover-bg": "#405023",
        "--scrollbar-thumb-bg": "#7f9f7f", "--scrollbar-track-bg": "#3d553d", "--placeholder-text": "#8a9a8a",
        "--dropdown-bg": "#4a6d4a", "--delete-color": "#cd5c5c", "--delete-hover-bg": "#b84c4c",
        "--popup-bg": "#4a6d4a", "--popup-text": "#e0e0d1", "--overlay-bg": "rgba(61, 85, 61, 0.7)",
        "--input-bg": "#6b8e6b", "--input-border": "#7f9f7f", "--input-text": "#e0e0d1",
        "--code-header-bg": "#6b8e6b", "--code-bg": "#304530", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#d3b393", "--blockquote-border": "#b8860b", "--blockquote-text": "#c4b8a8",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        "--syntax-keyword": "#b8860b", "--syntax-string": "#a3b86c", "--syntax-comment": "#8a9a8a",
        "--syntax-number": "#d8a070", "--syntax-function": "#8fbc8f", "--syntax-class": "#d3b393",
        "--syntax-tag": "#cd5c5c", "--syntax-attr": "#a3b86c", "--syntax-literal": "#d8a070"
    },
    "coffee": {
        "--bg-darkest": "#382f2f", "--bg-darker": "#4a3f3f", "--bg-dark-accent": "#5c4f4f", "--bg-light-accent": "#7d6f6f",
        "--text-light": "#dcd0ba", "--text-medium": "#b8a898", "--text-dark": "#382f2f",
        "--user-message-bg": "#a07c5b", "--button-primary-bg": "#8b6f4f", "--button-primary-hover-bg": "#6f583f",
        "--border-color": "#8a7a6a", "--icon-bar-bg": "#382f2f", "--icon-active-bg": "#c17c74",
        "--sidebar-hover-bg": "#7d6f6f", "--new-chat-bg": "#6b4f4f", "--new-chat-hover-bg": "#5a3f3f",
        "--scrollbar-thumb-bg": "#8a7a6a", "--scrollbar-track-bg": "#4a3f3f", "--placeholder-text": "#9a8a7a",
        "--dropdown-bg": "#5c4f4f", "--delete-color": "#c17c74", "--delete-hover-bg": "#a96a62",
        "--popup-bg": "#5c4f4f", "--popup-text": "#dcd0ba", "--overlay-bg": "rgba(74, 63, 63, 0.7)",
        "--input-bg": "#7d6f6f", "--input-border": "#8a7a6a", "--input-text": "#dcd0ba",
        "--code-header-bg": "#7d6f6f", "--code-bg": "#403535", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#e5ab76", "--blockquote-border": "#d1a377", "--blockquote-text": "#c4b49f",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        "--syntax-keyword": "#c17c74", "--syntax-string": "#a07c5b", "--syntax-comment": "#9a8a7a",
        "--syntax-number": "#d1a377", "--syntax-function": "#8b6f4f", "--syntax-class": "#e5ab76",
        "--syntax-tag": "#c17c74", "--syntax-attr": "#a07c5b", "--syntax-literal": "#d1a377"
    },
    "terminal": {
        "--bg-darkest": "#000000", "--bg-darker": "#0a0a0a", "--bg-dark-accent": "#1a1a1a", "--bg-light-accent": "#2a2a2a",
        "--text-light": "#00ff00", "--text-medium": "#00dd00", "--text-dark": "#0a0a0a",
        "--user-message-bg": "#00bb00", "--button-primary-bg": "#00aa00", "--button-primary-hover-bg": "#008800",
        "--border-color": "#333333", "--icon-bar-bg": "#000000", "--icon-active-bg": "#ff0000",
        "--sidebar-hover-bg": "#2a2a2a", "--new-chat-bg": "#009900", "--new-chat-hover-bg": "#007700",
        "--scrollbar-thumb-bg": "#333333", "--scrollbar-track-bg": "#0a0a0a", "--placeholder-text": "#444444",
        "--dropdown-bg": "#1a1a1a", "--delete-color": "#ff0000", "--delete-hover-bg": "#dd0000",
        "--popup-bg": "#1a1a1a", "--popup-text": "#00ff00", "--overlay-bg": "rgba(0, 0, 0, 0.7)",
        "--input-bg": "#2a2a2a", "--input-border": "#333333", "--input-text": "#00ff00",
        "--code-header-bg": "#2a2a2a", "--code-bg": "#000000", "--inline-code-bg": "var(--bg-light-accent)",
        "--inline-code-text": "#00ffff", "--blockquote-border": "#ffff00", "--blockquote-text": "#aaaa00",
        "--table-header-bg": "var(--bg-light-accent)", "--table-header-text": "var(--text-light)",
        "--syntax-keyword": "#00aa00", "--syntax-string": "#00ff00", "--syntax-comment": "#555555",
        "--syntax-number": "#00ffff", "--syntax-function": "#00dd00", "--syntax-class": "#ffff00",
        "--syntax-tag": "#ff0000", "--syntax-attr": "#00ff00", "--syntax-literal": "#00ffff"
    },
    "high-contrast": {
        "--bg-darkest": "#000000", "--bg-darker": "#080808", "--bg-dark-accent": "#111111", "--bg-light-accent": "#222222",
        "--text-light": "#ffffff", "--text-medium": "#eeeeee", "--text-dark": "#000000",
        "--user-message-bg": "#00ff00", "--button-primary-bg": "#00ffff", "--button-primary-hover-bg": "#00dddd",
        "--border-color": "#555555", "--icon-bar-bg": "#000000", "--icon-active-bg": "#ff00ff",
        "--sidebar-hover-bg": "#222222", "--new-chat-bg": "#ffff00", "--new-chat-hover-bg": "#dddd00",
        "--scrollbar-thumb-bg": "#666666", "--scrollbar-track-bg": "#080808", "--placeholder-text": "#777777",
        "--dropdown-bg": "#111111", "--delete-color": "#ff0000", "--delete-hover-bg": "#dd0000",
        "--popup-bg": "#111111", "--popup-text": "#ffffff", "--overlay-bg": "rgba(0, 0, 0, 0.8)",
        "--input-bg": "#222222", "--input-border": "#555555", "--input-text": "#ffffff",
        "--code-header-bg": "#222222", "--code-bg": "#000000", "--inline-code-bg": "#333333",
        "--inline-code-text": "#ffffff", "--blockquote-border": "#ffff00", "--blockquote-text": "#dddddd",
        "--table-header-bg": "#222222", "--table-header-text": "#ffffff",
        "--syntax-keyword": "#ff00ff", "--syntax-string": "#00ff00", "--syntax-comment": "#888888",
        "--syntax-number": "#00ffff", "--syntax-function": "#ffff00", "--syntax-class": "#ffff00",
        "--syntax-tag": "#ff0000", "--syntax-attr": "#00ff00", "--syntax-literal": "#00ffff"
    },
}


# --- Base CSS Structure (Selectors using variables) ---
# Includes structure for all components EXCEPT the removed icon bar
css_structure_template = """
/* Apply Theme Variables */

body { background-color: var(--bg-darkest); color: var(--text-light); }
.app-container { background-color: var(--bg-darker); }

/* Sidebar */
.sidebar { background-color: var(--bg-dark-accent); border-right: 1px solid var(--border-color); }
.sidebar-header { border-bottom: 1px solid var(--border-color); color: var(--text-light); }
.toggle-sidebar { color: var(--text-medium); }
.toggle-sidebar:hover { color: var(--text-light); }
.new-chat-button { background-color: var(--new-chat-bg); color: var(--text-light); }
/* Text color adjustments for light buttons */
.light-theme .new-chat-button, .solarized-light .new-chat-button, .sky .new-chat-button,
.high-contrast .new-chat-button, .terminal .new-chat-button /* Add themes with light buttons */ {
     color: #000000; /* Ensure contrast - usually black */
}
.dracula .new-chat-button, .monokai .new-chat-button, .nord .new-chat-button { color: #000000; } /* Dracula, Monokai, Nord often need black text on accent */
.dark .new-chat-button, .gruvbox-dark .new-chat-button, .solarized-dark .new-chat-button,
.ocean .new-chat-button, .forest .new-chat-button, .coffee .new-chat-button { color: #ffffff; } /* Ensure white for dark buttons */

.new-chat-button:hover { background-color: var(--new-chat-hover-bg); }

/* Chat List */
.chat-list-item:hover { background-color: var(--sidebar-hover-bg); }
.chat-list-item.active-chat { background-color: var(--button-primary-bg); color: var(--text-light); }
/* Text color adjustments for active list items */
.light-theme .chat-list-item.active-chat, .solarized-light .chat-list-item.active-chat, .sky .chat-list-item.active-chat,
.high-contrast .chat-list-item.active-chat { color: #000000; } /* Black text for high contrast active items */
.dark .chat-list-item.active-chat, .dracula .chat-list-item.active-chat, .monokai .chat-list-item.active-chat,
.nord .chat-list-item.active-chat, .gruvbox-dark .chat-list-item.active-chat, .solarized-dark .chat-list-item.active-chat,
.ocean .chat-list-item.active-chat, .forest .chat-list-item.active-chat, .coffee .chat-list-item.active-chat,
.terminal .chat-list-item.active-chat { color: #ffffff; } /* Ensure white text for dark active items */

.chat-list-item.active-chat:hover { background-color: var(--button-primary-bg); }
.chat-title { color: var(--text-medium); }
.chat-list-item.active-chat .chat-title { color: inherit; }
.chat-options-button { color: var(--text-medium); }
.chat-list-item:not(.active-chat) .chat-options-button:hover { background-color: var(--sidebar-hover-bg); color: var(--text-light); }
.chat-list-item.active-chat .chat-options-button { color: inherit; }
.chat-list-item.active-chat .chat-options-button:hover { background-color: rgba(0, 0, 0, 0.1); }
.light-theme .chat-list-item.active-chat .chat-options-button:hover,
.solarized-light .chat-list-item.active-chat .chat-options-button:hover,
.sky .chat-list-item.active-chat .chat-options-button:hover { background-color: rgba(255, 255, 255, 0.2); }
.high-contrast .chat-list-item.active-chat .chat-options-button:hover { background-color: #222; }

/* Dropdown */
.chat-options-dropdown { background-color: var(--dropdown-bg); border: 1px solid var(--border-color); }
.chat-options-dropdown button { color: var(--text-light); }
.chat-options-dropdown button:hover { background-color: var(--sidebar-hover-bg); color: var(--text-light); }
.chat-options-dropdown .delete-chat-button { color: var(--delete-color); }
.chat-options-dropdown .delete-chat-button:hover { background-color: var(--delete-hover-bg); color: var(--text-light); }
.light-theme .chat-options-dropdown .delete-chat-button:hover,
.solarized-light .chat-options-dropdown .delete-chat-button:hover,
.sky .chat-options-dropdown .delete-chat-button:hover { color: #ffffff; }
.high-contrast .chat-options-dropdown .delete-chat-button:hover { color: #ffffff;}

/* Placeholder */
.no-chats-placeholder { color: var(--text-medium); }

/* Main Chat Area */
.main-chat-area { background-color: var(--bg-darker); }
.chat-header { background-color: var(--bg-darker); border-bottom: 1px solid var(--border-color); color: var(--text-light); }
.settings-button { color: var(--text-medium); }
.settings-button:hover { color: var(--text-light); }

/* Messages */
.message-icon { color: var(--text-light); }
.user-message .message-icon { background-color: var(--user-message-bg); color: var(--text-light); }
.light-theme .user-message .message-icon, .solarized-light .user-message .message-icon, .sky .user-message .message-icon { color: #ffffff; }
.high-contrast .user-message .message-icon { color: #000000; }
.user-message .message-content { background-color: var(--user-message-bg); color: var(--text-light); }
.light-theme .user-message .message-content, .solarized-light .user-message .message-content, .sky .user-message .message-content { color: #ffffff; }
.high-contrast .user-message .message-content { color: #000000; }
.ai-message .message-icon { background-color: var(--bg-light-accent); color: var(--text-medium); }
.ai-message .message-content { background-color: var(--bg-light-accent); color: var(--text-light); }

/* Input Area */
#input-area { background-color: var(--bg-darker); border-top: 1px solid var(--border-color); }
#userInput { border: 1px solid var(--input-border); background-color: var(--input-bg); color: var(--input-text); }
#userInput::placeholder { color: var(--placeholder-text); }
#userInput:focus { border-color: var(--user-message-bg); }
#userInput:disabled { background-color: var(--bg-dark-accent); opacity: 0.7; }
.light-theme #userInput:disabled { background-color: var(--bg-light-accent); }
#sendButton { background-color: var(--button-primary-bg); color: var(--text-light); }
/* Text color adjustments for send button */
.light-theme #sendButton, .solarized-light #sendButton, .sky #sendButton,
.high-contrast #sendButton { color: #000000; } /* Black text */
.dark #sendButton, .dracula #sendButton, .monokai #sendButton, .nord #sendButton,
.gruvbox-dark #sendButton, .solarized-dark #sendButton, .ocean #sendButton,
.forest #sendButton, .coffee #sendButton, .terminal #sendButton { color: #ffffff; } /* White text */

#sendButton:hover { background-color: var(--button-primary-hover-bg); }
#sendButton:disabled { background-color: var(--input-bg); opacity: 0.6; }
#sendButton:disabled:hover { background-color: var(--input-bg); }

/* Loading Indicator */
#loading-indicator { background-color: var(--bg-darker); color: var(--placeholder-text); }

/* Scrollbars */
#chatbox::-webkit-scrollbar-track, .chat-list::-webkit-scrollbar-track { background: var(--scrollbar-track-bg); }
#chatbox::-webkit-scrollbar-thumb, .chat-list::-webkit-scrollbar-thumb { background-color: var(--scrollbar-thumb-bg); border: 2px solid var(--scrollbar-track-bg); }
#chatbox::-webkit-scrollbar-thumb:hover, .chat-list::-webkit-scrollbar-thumb:hover { background-color: var(--border-color); }
#chatbox, .chat-list { scrollbar-color: var(--scrollbar-thumb-bg) var(--scrollbar-track-bg); }

/* Settings Popup */
.popup-overlay { background-color: var(--overlay-bg); }
.popup { background-color: var(--popup-bg); color: var(--popup-text); }
.popup-header { border-bottom: 1px solid var(--border-color); }
.close-popup-button { color: var(--text-medium); }
.close-popup-button:hover { color: var(--text-light); }
.setting-item label { color: var(--popup-text); }
.setting-item select { background-color: var(--input-bg); border: 1px solid var(--input-border); color: var(--input-text); }
.setting-item select:focus { border-color: var(--user-message-bg); }
"""

# --- Markdown + Syntax Highlighting CSS Template (Using Variables) ---
markdown_syntax_template = """

/* --- Markdown Rendering Styles --- */

/* Code Blocks */
.message-content pre {
    background-color: var(--code-bg, rgba(0, 0, 0, 0.2));
    border: 1px solid var(--border-color);
    padding: 12px 15px;
    padding-top: 35px; /* Space for header */
    border-radius: 5px;
    overflow-x: auto;
    margin: 10px 0;
    font-size: 0.9em;
    color: var(--text-light); /* Default text inside code block */
    position: relative;
}
.message-content pre code { /* The actual code element */
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    background-color: transparent !important; /* Never have bg color */
    padding: 0;
    border: none;
    color: inherit; /* Inherit base color from pre */
    font-size: 1em;
    border-radius: 0;
    display: block; /* Ensure it takes block space */
    white-space: pre; /* Preserve whitespace */
}

/* Code Block Header */
.code-block-header {
    position: absolute;
    top: 0; left: 0; right: 0;
    background-color: var(--code-header-bg, rgba(255, 255, 255, 0.08));
    padding: 5px 15px;
    border-bottom: 1px solid var(--border-color);
    border-top-left-radius: inherit; border-top-right-radius: inherit;
    display: flex; justify-content: space-between; align-items: center;
    height: 35px;
}
.code-block-language { font-size: 0.8em; color: var(--text-medium); text-transform: lowercase; font-family: sans-serif; }
.copy-code-button { background: none; border: 1px solid transparent; color: var(--text-medium); cursor: pointer; padding: 3px 8px; font-size: 0.85em; border-radius: 4px; transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease; }
.copy-code-button:hover { background-color: rgba(255, 255, 255, 0.1); color: var(--text-light); border-color: var(--border-color); }
.light-theme .copy-code-button:hover, .solarized-light .copy-code-button:hover, .sky .copy-code-button:hover { background-color: rgba(0, 0, 0, 0.08); color: var(--text-dark); border-color: var(--border-color); }
.copy-code-button i { margin-right: 4px; }
.copy-code-button.copied { color: var(--user-message-bg); border-color: transparent; }
.light-theme .copy-code-button.copied, .solarized-light .copy-code-button.copied, .sky .copy-code-button.copied { color: var(--button-primary-bg); }

/* Inline Code */
.message-content p > code, .message-content li > code { background-color: var(--inline-code-bg, rgba(255, 255, 255, 0.1)); color: var(--inline-code-text, var(--text-light)); padding: 0.15em 0.4em; border-radius: 3px; font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace; font-size: 0.9em; }

/* Lists */
.message-content ul, .message-content ol { margin-left: 25px; margin-top: 8px; margin-bottom: 8px; color: var(--text-light); }
.message-content li { margin-bottom: 4px; }
.message-content li::marker { color: var(--text-medium); }

/* Bold / Italic */
.message-content strong, .message-content b { font-weight: bold; color: inherit; }
.message-content em, .message-content i { font-style: italic; color: inherit; }

/* Blockquotes */
.message-content blockquote { border-left: 3px solid var(--blockquote-border, var(--user-message-bg)); padding-left: 15px; margin: 10px 0 10px 5px; color: var(--blockquote-text, var(--text-medium)); font-style: italic; }
.message-content blockquote p { margin: 0; color: inherit; }

/* Tables */
.message-content table { border-collapse: collapse; margin: 15px 0; width: auto; border: 1px solid var(--border-color); font-size: 0.95em; }
.message-content th, .message-content td { border: 1px solid var(--border-color); padding: 8px 12px; text-align: left; color: var(--text-light); }
.message-content th { background-color: var(--table-header-bg, var(--bg-light-accent)); font-weight: bold; color: var(--table-header-text, var(--text-light)); }

/* Horizontal Rules */
.message-content hr { border: none; border-top: 1px solid var(--border-color); margin: 20px 0; }

/* --- Syntax Highlighting Overrides (Using Theme Variables) --- */
/* Apply to code within message content */
.message-content .hljs { color: inherit; background: transparent !important; } /* Inherit base color, ensure no hljs bg */
.message-content .hljs-comment, .message-content .hljs-quote { color: var(--syntax-comment, #888); font-style: italic; }
.message-content .hljs-keyword, .message-content .hljs-selector-tag, .message-content .hljs-subst { color: var(--syntax-keyword, #f92672); font-weight: normal; }
.message-content .hljs-number, .message-content .hljs-literal, .message-content .hljs-variable, .message-content .hljs-template-variable, .message-content .hljs-tag .hljs-attr { color: var(--syntax-number, #ae81ff); }
.message-content .hljs-string, .message-content .hljs-doctag { color: var(--syntax-string, #a6e22e); }
.message-content .hljs-title, .message-content .hljs-section, .message-content .hljs-selector-id { color: var(--syntax-function, #a6e22e); font-weight: normal; }
.message-content .hljs-subst { font-weight: normal; }
.message-content .hljs-type, .message-content .hljs-class .hljs-title { color: var(--syntax-class, #66d9ef); font-weight: normal; }
.message-content .hljs-tag, .message-content .hljs-name, .message-content .hljs-attribute { color: var(--syntax-tag, #f92672); font-weight: normal; }
.message-content .hljs-regexp, .message-content .hljs-link { color: var(--syntax-string, #a6e22e); } /* Use string color */
.message-content .hljs-symbol, .message-content .hljs-bullet { color: var(--syntax-tag, #f92672); } /* Use tag color */
.message-content .hljs-built_in, .message-content .hljs-builtin-name { color: var(--syntax-class, #66d9ef); } /* Use class color */
.message-content .hljs-meta { color: #999; font-weight: bold; }
.message-content .hljs-deletion { background: #fdd; }
.message-content .hljs-addition { background: #dfd; }
.message-content .hljs-emphasis { font-style: italic; }
.message-content .hljs-strong { font-weight: bold; }

/* Specific overrides for light themes if needed */
.light-theme .message-content .hljs-comment, .solarized-light .message-content .hljs-comment, .sky .message-content .hljs-comment { color: var(--syntax-comment, #6a737d); }
.light-theme .message-content .hljs-keyword, .solarized-light .message-content .hljs-keyword, .sky .message-content .hljs-keyword { color: var(--syntax-keyword, #7c4dff); }
.light-theme .message-content .hljs-string, .solarized-light .message-content .hljs-string, .sky .message-content .hljs-string { color: var(--syntax-string, #43a047); }
/* Add more light theme overrides if contrast is poor */


/* --- End Markdown & Syntax Highlighting Styles --- */
"""


# --- Script Logic ---
def create_theme_file(theme_name, color_palette):
    """Generates the CSS content for a single theme and writes the file."""
    print(f"Generating theme: {theme_name}...")
    # Determine if theme is light based on name (simple check)
    is_light_theme = "light" in theme_name.lower() or "sky" in theme_name.lower()

    root_definitions = ":root {\n"
    # Add a class to body for theme-specific overrides if needed (e.g., .light-theme)
    # No, better to handle overrides within the template using the name directly
    for var_name, value in color_palette.items():
        root_definitions += f"    {var_name}: {value};\n"
    root_definitions += "}\n\n"

    # Add theme-specific class to body selector for targeted overrides
    # This might conflict if multiple themes are loaded, but good for single theme context
    themed_body_selector = f"body.{theme_name} {{\n    /* Theme-specific body styles if needed */\n}}\n\n"
    # Safer approach: Use the existing .light-theme class check within templates

    # Add theme class context for overrides within the templates
    # The templates already use .light-theme etc where needed.

    css_content = f"/* static/themes/{theme_name}.css */\n\n"
    css_content += root_definitions
    # Add theme class wrapper? No, the JS should handle applying class to body if needed, or CSS uses :root vars.
    # css_content += f"body.{theme_name} {{\n" # Start theme wrapper - Not ideal
    css_content += css_structure_template
    css_content += markdown_syntax_template # Append Markdown AND Syntax styles
    # css_content += f"}} \n" # End theme wrapper - Not ideal

    file_path = os.path.join(themes_dir, f"{theme_name}.css")
    try:
        with open(file_path, "w", encoding="utf-8") as f: f.write(css_content)
        print(f"  Successfully created {file_path}")
    except IOError as e: print(f"  !! Error writing file {file_path}: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    try:
        os.makedirs(themes_dir, exist_ok=True)
        print(f"Ensured directory exists: {themes_dir}")
    except OSError as e: print(f"Error creating directory {themes_dir}: {e}"); exit()
    for name, palette in themes.items(): create_theme_file(name, palette)
    print("\nTheme file generation complete.")