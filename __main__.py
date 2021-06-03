# Import * from googleDriveAPI
from sys import argv
from googleDriveAPI.drive_list import driveCaller
import googleDriveAPI

# Check __name__ == "__main__.py ==> run main()"

if __name__ == "__main__":

    folder_id = argv[1]
    
    res = driveCaller(folder_id)
    
    print (res)