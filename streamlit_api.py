import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Title of the app
st.title("Title of Your Chatbot")

# Input text box
user_input = st.text_input("Ask a question:")

load_dotenv()
sourcID = os.environ.get('SOURCE_ID')
api_key = os.environ.get('API_KEY')


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