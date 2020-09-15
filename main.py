import event_creator

"""Instructions to get started:
Run quickstart.py, make sure credentials.json is in working directory.
This creates token.pickle so you can authenticate with calendar api.

The .gitignore file prevents git from pushing personal files.

The code I currently have creates a test event in my personal calendar.
Change calendar_id to your own.

https://developers.google.com/calendar/create-events
https://developers.google.com/calendar/quickstart/python
"""

# Template Event
event = {
    "summary": "Hello",
    "location": "Dedham, MA, 02026",
    "description": "This is a description",
    "start": {
        "dateTime": "2020-09-28T09:00:00-07:00",
        "timeZone": "America/New_York",
    },
    "end": {
        "dateTime": "2020-09-28T17:00:00-07:00",
        "timeZone": "America/New_York",
    }
}

if __name__ == "__main__":
    event_creator.new(event)
