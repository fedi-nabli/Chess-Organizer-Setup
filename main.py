from src.auth import AuthModule
from src.utils.get_files import DriveModule
from src.utils.get_values import get_values

def main():
  auth_session = AuthModule()
  drive  = DriveModule(auth_session.creds)
  get_values(drive.list_files()[2].get('id'), 'A1:B50', auth_session.creds)

if __name__ == '__main__':
  main()