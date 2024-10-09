import requests
import os
sourcID = os.environ.get('SOURCE_ID')
api_key = os.environ.get('API_KEY')

filename= 'YourFileName.pdf'

files = [
    ('file', ('file', open('/Files/'+filename, 'rb'), 'application/octet-stream')),
]

headers = {
    'x-api-key': api_key
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)