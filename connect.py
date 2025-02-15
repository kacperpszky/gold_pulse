import requests
import json
from urllib import request

def internet_on():
    try:
        request.urlopen('https://www.google.com/', timeout=1)
        return True
    except request.URLError as err: 
        return False

def make_request(date=""):
    api_key = "goldapi-6xe17m755wb44-io"
    symbol = "XAU"
    curr = "USD"
    date = date

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.text
    
        with open("api_results.txt", "w") as fp:
            fp.write(result)
            
        return result    
                
        
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        return None


def getData(key):
    try:
        with open("api_results.txt", "r") as fp:
            data = json.load(fp)
        
            if key in data:
                return data[key]  
            else:
                return 0      
                
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        return False  


