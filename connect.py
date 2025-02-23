import requests
import json
from urllib import request
import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "1009"
DB_HOST = "localhost"
DB_PORT = "5432"

def connectDB():
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        
        return True
    except:
        return False



def internet_on():
    try:
        request.urlopen('https://www.google.com/', timeout=1)
        return True
    except request.URLError as err: 
        return False

def make_request(date=""):
    api_key = "goldapi-3sjjsm7hoj4ds-io"
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


