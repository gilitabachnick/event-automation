import os
import requests
import datetime
import json
from dotenv import load_dotenv

# URL:
API_URL = "https://events-api.nvp1.ovp.kaltura.com/api/v1/event/create"

# Token:
load_dotenv()

TOKEN = os.getenv("KALTURA_TOKEN")

NUMBER_OF_EVENTS = int(os.getenv("NUMBER_OF_EVENTS", 2))  # How many events to create
DURATION_HOURS = int(os.getenv("DURATION_HOURS", 4))    # Duration of each event (in hours)


START_DATE = datetime.datetime.now(datetime.timezone.utc)


BASE_EVENT = {
    "templateId": os.getenv("TEMPLATE_ID","tm3000"),   # hard coded - depending on the event Type, each one creating a different event type: 000 blank, 1000 interactive, 2000 live webcast, 3000 Pre-recorded live, 4000 DIY live broadcast
    "description": os.getenv("DESCRIPTION"),
    "timezone": os.getenv("TIMEZONE", "America/New_York")
}

NAME_OF_EVENT = os.getenv("NAME_OF_EVENT", "AutoTest_")

# ===titles==
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json",
    "Content-Type": "application/json"
}

created_events = []

for i in range(1, NUMBER_OF_EVENTS + 1):
    start_date = START_DATE + datetime.timedelta(days=i - 1)
    end_date = start_date + datetime.timedelta(hours=DURATION_HOURS)

    event_data = BASE_EVENT.copy()
    event_data.update({
        "name": f"{NAME_OF_EVENT}{i}",
        "startDate": start_date.isoformat().replace("+00:00", "Z"),
        "endDate": end_date.isoformat().replace("+00:00", "Z")
    })

    print(f"\n sending the event: {event_data['name']}")
    response = requests.post(API_URL, headers=headers, json=event_data)

    if response.status_code in [200, 201]:
        print(f"✅ created successfully: {event_data['name']}")
        created_events.append({
            "name": event_data['name'],
            "startDate": event_data['startDate'],
            "endDate": event_data['endDate'],
            "response": response.json()
        })
    else:
        print(f"❌ failed to create {event_data['name']}: {response.status_code}")
        print(response.text)

# # ===== save as JSON =====
if created_events:
    with open("created_events.json", "w", encoding="utf-8") as f:
        json.dump(created_events, f, ensure_ascii=False, indent=4)
    print("\n The list of events created was saved on created_events.json")

print("\n Event creation complete!")
