from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)

print(response)

# Extract and print the URLs of the generated images
for image in response.data:
    print(image.url)