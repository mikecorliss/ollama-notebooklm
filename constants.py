"""
constants.py
"""

import os

from pathlib import Path

# Key constants
APP_TITLE = "Ollama NotebookLM 🎙️"
CHARACTER_LIMIT = 100_000

# Gradio-related constants
GRADIO_CACHE_DIR = "./gradio_cached_examples/tmp/"
GRADIO_CLEAR_CACHE_OLDER_THAN = 1 * 24 * 60 * 60  # 1 day

# Error messages-related constants
ERROR_MESSAGE_NO_INPUT = "Please provide at least one PDF file or a URL."
ERROR_MESSAGE_NOT_PDF = "The provided file is not a PDF. Please upload only PDF files."
ERROR_MESSAGE_NOT_SUPPORTED_IN_MELO_TTS = "The selected language is not supported without advanced audio generation. Please enable advanced audio generation or choose a supported language."
ERROR_MESSAGE_READING_PDF = "Error reading the PDF file"
ERROR_MESSAGE_TOO_LONG = "The total content is too long. Please ensure the combined text from PDFs and URL is fewer than {CHARACTER_LIMIT} characters."

# Ollama API-related constants
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MAX_TOKENS = 16_384
OLLAMA_MODEL_ID = "llama3.2"
OLLAMA_TEMPERATURE = 0.1
OLLAMA_JSON_RETRY_ATTEMPTS = 3

# MeloTTS
MELO_API_NAME = "/synthesize"
MELO_TTS_SPACES_ID = "mrfakename/MeloTTS"
MELO_RETRY_ATTEMPTS = 3
MELO_RETRY_DELAY = 5  # in seconds

MELO_TTS_LANGUAGE_MAPPING = {
    "en": "EN",
    "es": "ES",
    "fr": "FR",
    "zh": "ZJ",
    "ja": "JP",
    "ko": "KR",
}


# Suno related constants
SUNO_LANGUAGE_MAPPING = {
    "English": "en",
    "Chinese": "zh",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Polish": "pl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Spanish": "es",
    "Turkish": "tr",
}
SUNO_USE_SMALL_MODELS="True"

# General audio-related constants
NOT_SUPPORTED_IN_MELO_TTS = list(
    set(SUNO_LANGUAGE_MAPPING.values()) - set(MELO_TTS_LANGUAGE_MAPPING.keys())
)
NOT_SUPPORTED_IN_MELO_TTS = [
    key for key, id in SUNO_LANGUAGE_MAPPING.items() if id in NOT_SUPPORTED_IN_MELO_TTS
]

# Jina Reader-related constants
JINA_READER_URL = "https://r.jina.ai/"
JINA_RETRY_ATTEMPTS = 3
JINA_RETRY_DELAY = 5  # in seconds

# UI-related constants
UI_DESCRIPTION = """
Generate Podcasts from PDFs using open-source AI.

Built with:
- [Any model you wish on Ollama! 🐧](https://ollama.com/)
- [MeloTTS 🐚](https://huggingface.co/myshell-ai/MeloTTS-English)
- [Bark 🐶](https://huggingface.co/suno/bark)
- [Jina Reader 🔍](https://jina.ai/reader/)

**Note:** Only the text is processed (100k character limits).
"""
UI_AVAILABLE_LANGUAGES = list(set(SUNO_LANGUAGE_MAPPING.keys()))
UI_INPUTS = {
    "file_upload": {
        "label": "1. 📄 Upload your PDF(s)",
        "file_types": [".pdf"],
        "file_count": "multiple",
    },
    "url": {
        "label": "2. 🔗 Paste a URL (optional)",
        "placeholder": "Enter a URL to include its content",
    },
    "question": {
        "label": "3. 🤔 Do you have a specific question or topic in mind?",
        "placeholder": "Enter a question or topic",
    },
    "tone": {
        "label": "4. 🎭 Choose the tone",
        "choices": ["Fun", "Formal"],
        "value": "Fun",
    },
    "length": {
        "label": "5. ⏱️ Choose the length",
        "choices": ["Short (1-2 min)", "Medium (3-5 min)"],
        "value": "Medium (3-5 min)",
    },
    "language": {
        "label": "6. 🌐 Choose the language",
        "choices": UI_AVAILABLE_LANGUAGES,
        "value": "English",
    },
    "advanced_audio": {
        "label": "7. 🔄 Use advanced audio generation? (Experimental)",
        "value": True,
    },
}
UI_OUTPUTS = {
    "audio": {"label": "🔊 Podcast", "format": "mp3"},
    "transcript": {
        "label": "📜 Transcript",
    },
}
UI_API_NAME = "generate_podcast"
UI_ALLOW_FLAGGING = "never"
UI_CONCURRENCY_LIMIT = 3
UI_EXAMPLES = [
    [
        [str(Path("examples/1310.4546v1.pdf"))],
        "",
        "Explain this paper to me like I'm 5 years old",
        "Fun",
        "Short (1-2 min)",
        "English",
        True,
    ],
    [
        [],
        "https://en.wikipedia.org/wiki/Hugging_Face",
        "How did Hugging Face become so successful?",
        "Fun",
        "Short (1-2 min)",
        "English",
        False,
    ],
    [
        [],
        "https://simple.wikipedia.org/wiki/Taylor_Swift",
        "Why is Taylor Swift so popular?",
        "Fun",
        "Short (1-2 min)",
        "English",
        False,
    ],
]
UI_CACHE_EXAMPLES = True
UI_SHOW_API = True
