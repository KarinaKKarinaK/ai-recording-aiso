# 🎙️ Audio to Blog Post Converter

A Streamlit web app that turns long audio recordings into readable blog-style posts using Whisper for transcription and BART for summarization.

## Features
- Upload MP3/WAV/M4A files
- Transcribes using Whisper
- Summarizes with Hugging Face transformers
- Clean, user-friendly Streamlit UI

## Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/audio_to_blog_app.git
cd audio_to_blog_app
pip install -r requirements.txt
streamlit run app.py
