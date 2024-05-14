from openai import OpenAI
from dotenv import load_dotenv
import base64
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = os.path.join(os.path.dirname(__file__), "image.jpeg")

# Getting the base64 string
base64_image = encode_image(image_path)

# Create a completion request
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an assistant that analyzes images and provides detailed information."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What’s in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        },
        {
            "role": "system",
            "content": "Extract text in the original language"
        },
        {
            "role": "system",
            "content": "Translate extracted text to English"
        }
    ],
    max_tokens=1000
)

# Print the response
print(completion.choices[0].message)
