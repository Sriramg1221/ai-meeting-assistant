import whisper
from summarizer import summarize_meeting

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Model loaded successfully!")

def transcribe_audio(audio_path):

    print(f"Transcribing: {audio_path}")

    result = model.transcribe(audio_path)

    return result["text"]

if __name__ == "__main__":

    audio_file = "audio-notes/sample.mp3"

    transcript = transcribe_audio(audio_file)

    print("\nTRANSCRIPT:\n")
    print(transcript)

    print("\nGENERATING MEETING SUMMARY...\n")

    summary = summarize_meeting(transcript)

    print(summary)