from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

load_dotenv()

def formulate_output(city, province, country, start_date, num_days, start_time, end_time):
    # city="Saguenay" # including city can be optional
    # province="Quebec" 
    # country="Canada"
    # start_date="Feb 17, 2025"
    # end_date="Feb 19, 2025" # including end_date can be optional
    # start_time="10:00"
    # end_time="23:00"

    # template for a single day of planning
    example_json = {
        "day": "13",
        "month": "11",
        "year": "2025",
        "events": [
        {
            "title": "Visit Richmond Green Sports Centre and Park",
            "time": "10:00",
            "location": "Canada"
        },
        {
            "title": "Relax at Mill Pond Park",
            "time": "11:00",
            "location": "Canada"
        },
        {
            "title": "Enjoy a movie at SilverCity Richmond Hill",
            "time": "13:00",
            "location": "Canada"
        }
        ],
    }

    location_option_1=(f"{city} in {country}")
    if province != "":
        location_option_1 = (f"{city}, {province} in {country}")

    date_option=(f"on {start_date}")
    quantifier_option=(f"For that day")

    date_option=(f"from {start_date} to {num_days} days later")
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
            "time": "10:00",
            "location": "Canada"
        },
        {
            "title": "Relax at Mill Pond Park",
            "time": "11:00",
            "location": "Canada"
        },
        {
            "title": "Enjoy a movie at SilverCity Richmond Hill",
            "time": "13:00",
            "location": "Canada"
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
            "time": "10:00",
            "location": "Canada"
        },
        {
            "title": "Lunch at Touro Steakhouse",
            "time": "14:00 AM",
            "location": "Canada"
        },
        {
            "title": "Stargazing at David Dunlap Observatory",
            "time": "21:00",
            "location": "Canada"
        }
        ],
        }
    }

    outline_prompt = (
        f'I am going to {location_option_1}, {date_option}. '
        f'{quantifier_option}, schedule what events/places I should do ONLY in {city} from {start_time} to {end_time}. ' 
        f'Please provide the response ONLY in JSON format, AND NOTHING ELSE.'
    )

    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Provide output in valid JSON. The data schema should be like this: " + json.dumps(example_json)},
        {"role": "user", "content": outline_prompt},
        {"role": "system", "content": "Provide output in valid JSON. The data schema should be like this: " + json.dumps(example_json)},
        {"role": "user", "content": outline_prompt},
        ]
    )

    output = response.choices[0].message.content
    return output

app = Flask(__name__)
CORS(app)

@app.route("/process", methods=['POST'])
def process():
    data = request.get_json()
    city = data.get('city')
    province = data.get('province')
    country = data.get('country')
    start_date = "" + str(data.get('start_month')) + " " + str(data.get('start_day')) + ", " + str(data.get('start_year'))
    num_days = data.get('num_days')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    response = formulate_output(city, province, country, start_date, num_days, start_time, end_time)
    
    return "jsonify(response))"
# json_object = json.loads(output)

# print(json_object)




# json_object = json.loads(output)

# print(json_object)

if __name__ == "__main__":
    app.run(debug=True)