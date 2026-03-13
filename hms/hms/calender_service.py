from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def create_event(summary,start,end):

    creds = Credentials.from_authorized_user_file('token.json')

    service = build('calendar','v3',credentials=creds)

    event = {
        'summary': summary,
        'start': {'dateTime': start},
        'end': {'dateTime': end},
    }

    service.events().insert(
        calendarId='primary',
        body=event
    ).execute()