from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()




client = OpenAI()
response = client.chat.completions.create(
model="gpt-4",
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "I am going to Richmond Hill, Ontario starting from February 16-20. For each day, schedule what events/places I should do ONLY in Richmond Hill from 11am-11pm. Please provide the response in JSON format"},
    ]
)

output = response.choices[0].message.content
print(output)