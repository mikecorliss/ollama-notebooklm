---
title: Open NotebookLM
emoji: 🎙️
colorFrom: purple
colorTo: red
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
short_description: Personalised Podcasts For All - Available in 13 Languages
---

# Open NotebookLM

## Overview

This project is inspired by the NotebookLM tool, and implements it with open-source LLMs and text-to-speech models. This tool processes the content of a PDF, generates a natural dialogue suitable for an audio podcast, and outputs it as an MP3 file.

Built with:
- [Any model you wish on Ollama! 🐧](https://ollama.com/)
- [MeloTTS 🐚](https://huggingface.co/myshell-ai/MeloTTS-English)
- [Bark 🐶](https://huggingface.co/suno/bark)
- [Jina Reader 🔍](https://jina.ai/reader/)

## Features

- **Convert PDF to Podcast:** Upload a PDF and convert its content into a podcast dialogue.
- **Engaging Dialogue:** The generated dialogue is designed to be informative and entertaining.
- **User-friendly Interface:** Simple interface using Gradio for easy interaction.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mikecorliss/ollama-notebooklm.git
   cd open-notebooklm
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Update constants.py:**
   In my fork, i've moved everything to ollama,
   as it utilizes the same openai api interface.
   Update your model you're using, and change the URL
   if you're not hosting it on the machine or on a different port.

3. **Run the application:**
   ```bash
   python app.py
   ```
   This will launch a Gradio interface in your web browser.

4. **Upload a PDF:**
   Upload the PDF document you want to convert into a podcast.

5. **Generate Audio:**
   Click the button to start the conversion process. The output will be an MP3 file containing the podcast dialogue.

## Acknowledgements

This project is forked from [`gabrielchua/open-notebooklm`](https://github.com/gabrielchua/open-notebooklm)

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more information.
