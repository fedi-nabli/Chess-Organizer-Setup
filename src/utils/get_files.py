from __future__ import print_function

# Google APIs Imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class DriveModule():
  def __init__(self, creds: Credentials = None) -> None:
    self.creds = creds

    try:
      self.services = build('drive', 'v3', credentials=creds)
      results = self.services.files().list(
        pageSize = 10, fields='nextPageToken, files(id, name)'
      ).execute()
      self.items = results.get('files', [])

      if not self.items:
        print('No items found')
        return
      # print('Files:')
      # for item in self.items:
      #   print(u'{0} ({1})'.format(item['name'], item['id']))
    
    except HttpError as error:
      print(f'An error occured: {error}')

  def list_files(self) -> list:
    try:
      files = []
      page_token = None
      while True:
        response = self.services.files().list(
          q="mimeType='application/vnd.google-apps.spreadsheet'",
          spaces='drive',
          fields='nextPageToken, '
                  'files(id, name)',
          pageToken=page_token
        ).execute()

        for file in response.get('files', []):
          print(f'Found file: {file.get("name")}, {file.get("id")}')
        files.extend(response.get('files', []))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
          break
    except HttpError as error:
      print(f'An error occured: {error}')
      file = None

    return files