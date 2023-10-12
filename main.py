from src.auth import AuthModule
from src.utils.get_files import DriveModule
from src.utils.get_values import SpreadsheetModule

def main():
  auth_session = AuthModule()
  drive  = DriveModule(auth_session.creds)
  spreadsheets = drive.list_files()
  spreadsheet_instance = SpreadsheetModule(auth_session.creds)
  spreadsheet_instance.get_values(spreadsheets[2].get('id'), 'A1:B50')

if __name__ == '__main__':
  main()