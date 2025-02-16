from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()


city="Saguenay" # including city can be optional
province="Quebec" 
country="Canada"
start_date="Feb 17, 2025"
end_date="Feb 19, 2025" # including end_date can be optional
start_time="10am"
end_time="11pm"

# template for a single day of planning
example_json = {
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
}




location_option_1=(f"{province} in {country}")
location_option_2=(f"{province}")
if city != "":
    location_option_1 = (f"{city}, {province} in {country}")
    location_option_2=(f"{city}")


date_option=(f"on {start_date}")
quantifier_option=(f"For that day")

if end_date != "":
    date_option=(f"from {start_date} to {end_date}")
    quantifier_option=(f"For each day")

    # template for 1-3 days of planning
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
    f'I am going to {location_option_1}, {date_option}. '
    f'{quantifier_option}, schedule what events/places I should do ONLY in {location_option_2} {date_option}. ' 
    f'Please provide the response ONLY in JSON format, AND NOTHING ELSE.'
)
print(outline_prompt)

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


