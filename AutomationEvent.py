
import requests
import datetime
import json

# URL:
API_URL = "https://events-api.nvp1.ovp.kaltura.com/api/v1/event/create"

# Token:
TOKEN = ""

NUMBER_OF_EVENTS = 10  # How many events to create
DURATION_HOURS = 4    # Duration of each event (in hours)


START_DATE = datetime.datetime.now(datetime.timezone.utc)

BASE_EVENT = {
    "templateId": "tm3000",   # hard coded - depending on the event Type, each one creating a different event type 
    "description": "Automation via API",
    "timezone": "America/New_York"
}

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
        "name": f"AutoTest_{i}",
        "startDate": start_date.isoformat().replace("+00:00", "Z"),
        "endDate": end_date.isoformat().replace("+00:00", "Z")
    })

    print(f"\n sending the event: {event_data['name']}")
    response = requests.post(API_URL, headers=headers, json=event_data)

    if response.status_code in [200, 201]:
        print(f"✅ created successfullyה: {event_data['name']}")
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
