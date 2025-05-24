import streamlit as st
from groq import Groq
st.set_page_config(page_title="Audio-to-speech", page_icon="", layout="centered")

# Streamlit UI
st.title("🎙️ Audio to Text avec Groq Whisper Large V3 🚀")
st.write("Upload ton fichier audio et récupère la transcription directe.")

# Champ pour entrer la clé API Groq
api_key = st.text_input("🔑 Entre ta clé API Groq :", type="password")

# Init Groq client si clé fournie
if api_key:
    client = Groq(api_key=api_key)

    # Upload audio
    audio_file = st.file_uploader("📤 Upload un fichier audio (mp3, wav, m4a)", type=["mp3", "wav", "m4a"])

    # Function pour transcrire
    def transcribe_audio(file):
        with st.spinner("📝 Transcription en cours..."):
            transcription = client.audio.transcriptions.create(
                file=(file.name, file.read()),
                model="whisper-large-v3",
                prompt="Specify context or spelling",  # facultatif
                response_format="json",
                language="en",
                temperature=0.0
            )
        return transcription.text

    # Action sur upload
    if audio_file is not None:
        transcription_text = transcribe_audio(audio_file)
        st.success("✅ Transcription terminée")
        st.write("**📝 Texte détecté :**")
        st.write(transcription_text)

        # Bouton pour télécharger le transcript
        st.download_button(
            label="📥 Télécharger la transcription",
            data=transcription_text,
            file_name="transcript.txt",
            mime="text/plain"
        )

else:
    st.warning("💡 Entre ta clé API Groq pour activer la transcription.")
