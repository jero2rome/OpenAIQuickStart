from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

response = client.images.generate(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)

print(response)

# Extract and print the URLs of the generated images
for image in response.data:
    print(image.url)