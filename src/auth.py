from __future__ import print_function
import os.path

# Google auth imports
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class AuthModule():
  def __init__(self) -> None:
    self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    self.creds = None
    if os.path.exists('token.json'):
      self.creds = Credentials.from_authorized_user_file('token.json', scopes=self.SCOPES)
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
        self.creds = flow.run_local_server(port=0)
      with open('token.json', 'w') as token:
        token.write(self.creds.to_json())