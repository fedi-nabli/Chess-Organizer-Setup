from __future__ import print_function

# Google imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class SpreadsheetModule():
  def __init__(self, creds: Credentials) -> None:
    try:
      self.services = build('sheets', 'v4', credentials=creds)
      print('Initiated sheets module successfully')

    except HttpError as error:
      print(f'An error occured: {error}')

  def get_values(self, spreadsheet_id, range_name):
    try:
      result = self.services.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name
      ).execute()

      rows = result.get('values', [])
      print(f'{len(rows)} retrieved')
      print(rows)
      return rows

    except HttpError as error:
      print(f'An error occured: {error}')
      return error