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
KALTURA_TOKEN=your_token_here
NUMBER_OF_EVENTS=x
DURATION_HOURS=y

### 2. Install dependencies
Install the required Python packages using:

```bash
pip install -r requirements.txt
