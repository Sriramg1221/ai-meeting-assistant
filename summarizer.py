from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize_meeting(transcript):

    prompt = f"""
    You are an AI executive meeting assistant.

    Analyze the following transcript and generate:

    1. Meeting Summary
    2. Key Discussion Points
    3. Decisions Taken
    4. Action Items
    5. Next Steps
    6. Minutes of Meeting

    Keep output professional and structured.

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content