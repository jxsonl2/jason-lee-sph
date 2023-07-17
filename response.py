import requests
import csv
 
url = "https://www.google.com"
 
response = requests.get(url)
 
print(response.status_code)
