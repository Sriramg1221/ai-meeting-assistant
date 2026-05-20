import streamlit as st
import whisper
from summarizer import summarize_meeting

# Load Whisper model
model = whisper.load_model("base")

# Page title
st.title("AI Meeting Assistant")

st.write("Upload a meeting audio file to generate summaries and action items.")

# Upload audio file
uploaded_file = st.file_uploader(
    "Upload Audio File",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file is not None:

    # Save uploaded audio temporarily
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.read())

    st.success("Audio uploaded successfully!")

    # Transcription
    st.subheader("Transcribing Audio...")

    result = model.transcribe("temp_audio.mp3")

    transcript = result["text"]

    st.subheader("Transcript")
    st.write(transcript)

    # Summarization
    st.subheader("Generating AI Meeting Notes...")

    summary = summarize_meeting(transcript)

    st.subheader("AI Meeting Summary")
    st.markdown(summary)