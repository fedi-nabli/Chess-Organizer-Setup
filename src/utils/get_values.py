from __future__ import print_function

# Google imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_values(spreadsheet_id, range_name, creds: Credentials):
  try:
    services = build('sheets', 'v4', credentials=creds)
    result = services.spreadsheets().values().get(
      spreadsheetId=spreadsheet_id, range=range_name
    ).execute()

    rows = result.get('values', [])
    print(f'{len(rows)} retrieved')
    print(rows)
    return rows

  except HttpError as error:
    print(f'An error eccured: {error}')
    return error