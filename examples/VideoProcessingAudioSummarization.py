from openai import OpenAI
from dotenv import load_dotenv
import os
from utilities import process_video

# We'll be using the OpenAI DevDay Keynote Recap video. You can review the video here: https://www.youtube.com/watch?v=h02ti0Bl6zk
# Only 30secs of the video is processed in this example to keep under the 1min limit for OpenAI API
VIDEO_PATH = os.path.join(os.path.dirname(__file__), "data", "keynote_recap.mp4")

# Load environment variables from .env file
load_dotenv()

MODEL="gpt-4o"
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Extract 1 frame per second. You can adjust the `seconds_per_frame` parameter to change the sampling rate
base64Frames, audio_path = process_video(VIDEO_PATH, seconds_per_frame=1)

# Transcribe the audio
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=open(audio_path, "rb"),
)

print("Transcript: ", transcription.text + "\n\n")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
    {"role": "system", "content":"""You are generating a transcript summary. Create a summary of the provided transcription. Respond in Markdown."""},
    {"role": "user", "content": [
        {"type": "text", "text": f"The audio transcription is: {transcription.text}"}
        ],
    }
    ],
    temperature=0,
)
print(response.choices[0].message.content)