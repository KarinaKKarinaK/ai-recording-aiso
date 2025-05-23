import streamlit as st
from transcriber import transcribe_audio
from summarizer import summarize_text
import tempfile

st.title("🎙️ Audio to Blog Post Converter")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.info("Transcribing audio...")
    transcription = transcribe_audio(tmp_path)
    st.success("Transcription complete!")

    st.subheader("📝 Transcription")
    st.text_area("Raw Text", transcription, height=200)

    st.info("Generating blog post...")
    blog_post = summarize_text(transcription)
    st.success("Blog post ready!")

    st.subheader("📄 Blog Post")
    st.text_area("Blog Text", blog_post, height=300)
