from __future__ import print_function
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
    
# take file name and remove file extention
# def getTitle(file):
#     # remove extension from file name 
#     print(file[:-4:].replace('.',' '))

# specify  folder to list contents from
def driveCaller(folder_id):

    ''' google api stuff '''
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly.metadata'
    store = file.Storage('storage.json') 
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    query = f"parents =  '{folder_id}'"
    ''' google api stuff '''

    # return files in specified folder
    return DRIVE.files().list(q=query).execute().get('files', {})