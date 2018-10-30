from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

print('This is the feed of stuff!')

SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'

def main():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('creds.json', SCOPE)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('no labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
    

if __name__ == '__main__':
    main()
