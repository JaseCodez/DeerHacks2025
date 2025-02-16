from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
response = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Give me 10 ideas for a Youtube channel about Python"},
    ]
)

output = response.choices[0].message.content
print(output)