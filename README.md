# CV-GPT an Open-Source AI ChatBot for Your CV [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This GitHub repository allows you to build an AI chatbot based off your CV (or any other relevant documents) that can then be hosted online for others to access and query about your work.

# Quick-Start (Local Machine)
The first stage is to clone this repository on your local machine using the following bash command:
```
git clone https://github.com/cja119/CVGpt.git
```
Then install the necessary dependencies using pip:
```
pip install -r requirements.txt
```
Next, navigate to [ChatPdf](https://www.chatpdf.com/), scroll to the bottom of the webpage, create an account and follow the steps to generate an API Key. Their free service allows for 5000 pdf pages to be read and 500 queries to your custom LLM per month. Once complete, save this key to the .env file located in the repository in the format (ensure no spaces):
```
API_KEY="Your_API_Key"
```
Whilst in this folder, add the name you want for your chatbot as an environment variable:
```
API_NAME="Your Api Name"
```
Then, save your pdf file in the '/Files/' folder located in the repository and then run the following bash script (do not include the path in the filename):
```
python setup_files.py "YourFileName" 
```
You're now ready to run your chatbot (note you can modify the title of your chatbot in the streamlit_api.py file:
```
streamlit run streamlit_api.py
```
# Web Hosted
For webhosting, follow the steps above (this generates some environment variables pertaining to your pdf file which you will need to store on your online server). The first step is to setup a free account on [Render](https://render.com/). Once setup, sign in, select 'Web Service' under the 'new' tab in the top right hand of the screen. Click clone from public repository and paste the following link:
```
https://github.com/cja119/CVGpt.git
```
Once finished, click create. Add a name for your API. Then, scroll down and, under start command, paste the following command:
```
streamlit run streamlit_api.py --server.port $PORT
```
The payed service for Render is optional, this can run effectively off their free service. Scroll to the bottom and under environment variables, select 'add from .env' and paste the contents of the .env file on you local repository. If the quick start steps have been followed successfully, there should be three variables:
```
API_KEY="Your_API_Key"
API_NAME="Your Api Name"
SOURCE_ID="YourSourceID
```
Finally, click deploy API.


