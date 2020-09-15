from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

import datetime
import os.path
import pickle


def new(event: dict, calendar_id="primary"):
    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    try:
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    except FileNotFoundError:
        print("'credentials.json' not found. Download it from https://developers.google.com/calendar/quickstart/python and run quickstart.py.")
        exit()

    service = build("calendar", "v3", credentials=creds)
    service.events().insert(calendarId=calendar_id, body=event).execute()
    