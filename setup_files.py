import requests
import os
import sys
from dotenv import load_dotenv, set_key

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
api_key = os.environ.get('API_KEY')

filename= sys.argv[1]

files = [
    ('file', ('file', open('/Files/'+filename, 'rb'), 'application/octet-stream')),
]

headers = {
    'x-api-key': api_key
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    source_id = response.json()['sourceId']
    print('Source ID:', source_id)
    
    # Save the source ID to .env file
    set_key(env_path, 'SOURCE_ID', source_id)
else:
    print('Status:', response.status_code)
    print('Error:', response.text)

