from IPython.display import Image, display, Audio, Markdown
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

# Load environment variables from .env file
load_dotenv()

MODEL="gpt-4o"
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Path to your image
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "data", "triangle.png")

# Preview image for context
display(Image(IMAGE_PATH))

# Open the image file and encode it as a base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image(IMAGE_PATH)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in Markdown. Help me with my math homework!"},
        {"role": "user", "content": [
            {"type": "text", "text": "What's the area of the triangle?"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)
