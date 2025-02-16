from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()


city="Richmond"
province="British Columbia"
country="Canada"
start_date="February 16, 2025"
end_date="February 20, 2025"
start_time="11am"
end_time="11pm"


example_json = {
   "day 1": {
     "day": "13",
     "month": "11",
     "year": "2025",
     "events": [
       {
           "title": "Visit Richmond Green Sports Centre and Park",
           "time": "10:00 AM",
       },
       {
           "title": "Relax at Mill Pond Park",
           "time": "11:00 AM",
       },
       {
           "title": "Enjoy a movie at SilverCity Richmond Hill",
           "time": "1:00 PM"
       }
     ],
  },
    "day 2": {
    "day": "14",
    "month": "11",
    "year": "2025",
    "events": [
    {
        "title": "Explore Oak Ridges Moraine",
        "time": "10:00 AM",
    },
    {
        "title": "Lunch at Touro Steakhouse",
        "time": "11:00 AM",
    },
    {
        "title": "Stargazing at David Dunlap Observatory",
        "time": "1:00 PM"
    }
    ],
    }
}


outline_prompt = (
    f'I am going to {city}, {province} in {country}, starting from {start_date} to {end_date}. '
    f'For each day, schedule what events/places I should do ONLY in {city} from {start_time} to {end_time}. ' 
    f'Please provide the response ONLY in JSON format, AND NOTHING ELSE.'
)

client = OpenAI()
response = client.chat.completions.create(
model="gpt-4",
messages=[
    {"role": "system", "content": "Provide output in valid JSON. The data schema should be like this: " + json.dumps(example_json)},
    {"role": "user", "content": outline_prompt},
    ]
)

output = response.choices[0].message.content
print(output)

json_object = json.loads(output)

print(json_object)


