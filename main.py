from src.auth import AuthModule
from src.utils.get_files import DriveModule

def main():
  auth_session = AuthModule()
  drive  = DriveModule(auth_session.creds)
  drive.list_files()

if __name__ == '__main__':
  main()