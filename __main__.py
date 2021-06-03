# Import * from googleDriveAPI
from sys import argv
from googleDriveAPI.drive_list import driveCaller
import googleDriveAPI

# Check __name__ == "__main__.py ==> run main()"

if __name__ == "__main__":

    try:
        # exampel folder id "0B69RRb17QL4pflctSUpZYmlScVlMNmFKVnFuS1RLT1BHR1BGZkR2eW5YYmhiQlZMSmo2Nm8"
        # Specify the folder 
        # Get user input
        print ('\nEnter folder id: \n')
        folder_id = input()
        res = driveCaller(folder_id)
        print ('\nYour output =>\n')
        print (res)
        print ('\n ... sending output to file\n\n')

        # write contents to file 
        f = open('filecontents.txt','w')
        f.write(str(res))
        f.close()
    except:

        print ('error has occured')



        
    