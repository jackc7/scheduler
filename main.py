import datetime
import pickle
import os.path
import quickstart
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# https://developers.google.com/calendar/create-events
# https://developers.google.com/calendar/quickstart/python

print()

SCOPES = ["https://www.googleapis.com/auth/calendar"]
calendar_id = "primary" # Main calendar is "primary"

"""Instructions to get started:
Run quickstart.py, make sure credentials.json is in working directory.
This creates token.pickle so you can authenticate with calendar api.

The .gitignore file prevents git from pushing personal files.

The code I currently have creates a test event in my personal calendar.
Change calendar_id to your own.
"""

try:
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)
except:
    quickstart.main()
    
service = build("calendar", "v3", credentials=creds)


event = {
    "summary": "Test",
    "location": "Dedham, MA, 02026",
    "description": "Test",
    "start": {
        "dateTime": "2020-09-28T09:00:00-07:00",
        "timeZone": "America/New_York",
    },
    "end": {
        "dateTime": "2020-09-28T17:00:00-07:00",
        "timeZone": "America/New_York",
    },
}

service.events().insert(calendarId=calendar_id, body=event).execute()

class Data:
    """Days school is on and days its off.
    Starts August 30, 2020
    https://www.dedham.k12.ma.us/cms/lib/MA02213180/Centricity/ModuleInstance/2803/20%2021%20Dedham%20School%20Calendar.pdf
    """

    DAY = [0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 0, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 0, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 0, 0, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0,
           0, 1, 1, 0, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 0, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 0, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 0, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 0, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0,
           0, 1, 1, 1, 1, 1, 0]

    
    PATTERN = [[1, 7, 6, 5, 4],
               [3, 2, 1, 7, 6],
               [5, 4, 3, 2, 1],
               [7, 6, 5, 4, 3],
               [2, 1, 7, 6, 5],
               [4, 3, 2, 1, 7],
               [6, 5, 4, 3, 2]]


if __name__ == "__main__":
    pass
