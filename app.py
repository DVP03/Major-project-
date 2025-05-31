import os
import whisper
import streamlit as st
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def text_to_speech(text, output_audio_path, language):
    tts = gTTS(text=text, lang=language)
    tts.save(output_audio_path)
    return output_audio_path

def convert_audio(input_audio, target_language, output_audio):
    text = transcribe_audio(input_audio)
    translated_text = translate_text(text, target_language)
    text_to_speech(translated_text, output_audio, target_language)
    return output_audio

st.title("Audio Translator App")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Punjabi": "pa"
}

target_language = st.selectbox("Choose language:", list(languages.keys()))

if uploaded_file is not None:
    if st.button("Translate Audio"):
        input_audio_path = "input_audio.mp3"
        output_audio_path = "translated_audio.mp3"
        
        with open(input_audio_path, "wb") as f:
            f.write(uploaded_file.read())
        
        st.text("Processing audio...")
        translated_audio = convert_audio(input_audio_path, languages[target_language], output_audio_path)
        
        st.audio(translated_audio, format="audio/mp3")
        st.success("Translation Complete! Play the translated audio above.")
