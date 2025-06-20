import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

genai.configure(api_key="AIzaSyDwfbKNWSRjX9cNsbh60-09Qk8zD83mvKY")
model = genai.GenerativeModel('gemini-2.0-flash')

def fetch_job_description(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Failed to load page")

        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.body
        if body is None:
            raise Exception("No <body> tag found on page")

        # Extract all text, separated by newlines for readability
        full_text = body.get_text(separator='\n').strip()
        return full_text
    
    except:
        print("Error in fetching...")

if __name__ == "__main__":
    # Example usage:
    url = str(input("Enter the job website / description : "))

    if url[0:4] == "http":
        description = fetch_job_description(url)
    else: 
        description = url
    print(description)

###need to change main as development goes further
