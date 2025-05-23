# transcriber.py
import whisper

def transcribe_audio(file_path: str) -> str:
    model = whisper.load_model("base")  # use "medium" or "large" for better quality
    result = model.transcribe(file_path)
    return result["text"]
