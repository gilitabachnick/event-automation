# Event Automation Script

This Python script automates the creation of events using the Kaltura Events API.

## Features
- Create multiple events automatically
- Configurable number of events and duration
- Uses `.env` file for secure token and settings
- Saves created events to `created_events.json`

## Requirements
- Python 3.12+
- Packages: `requests`, `python-dotenv`

### Setup
1. Ensure you have a `.env` file with your Kaltura token and settings, e.g.:
KALTURA_TOKEN=""
NUMBER_OF_EVENTS=2  
DURATION_HOURS=4
TEMPLATE_ID=tm3000
DESCRIPTION=Automation via API
TIMEZONE=America/New_York
NAME_OF_EVENT=""


### 2. Install dependencies
Install the required Python packages using:

```bash
pip install -r requirements.txt
