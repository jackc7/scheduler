from googleapiclient.discovery import build
import pickle


def new(event: dict, calendar_id=None):    
    """Creates a single event on your Calendar."""

    try:
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    except FileNotFoundError:
        print("'token.pickle' not found. Run quickstart.py to generate it.")
        exit()

    service = build("calendar", "v3", credentials=creds)
    service.events().insert(calendarId=calendar_id, body=event).execute()
