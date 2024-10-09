import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
sourcID = os.environ.get('SOURCE_ID')
api_key = os.environ.get('API_KEY')
api_name = os.environ.get('API_NAME')

# Title of the app
st.title(api_name)

# Input text box
user_input = st.text_input("Ask a question:*")
st.caption("*Some answers may be inaccurate due to the probabilistic/uncertain nature of large language model responses. If you have any questions, please feel free to reach out to me directly.")



headers = {
    'x-api-key': api_key
}


data = {
  "sourceId": sourcID,
  "messages": [
    {
      "role": "user",
      "content": user_input
    }
  ]
}

# Submit button
if st.button("Submit"):
    response = requests.post(
        'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)
        # Display the output
    if response.status_code == 200:
        st.write('Response:', response.json()['content'])
    else:
        st.write('Error:', response.json()['error'])
