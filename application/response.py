import requests
import pandas as pd
from datetime import datetime


## "import" the CSV file
df = pd.read_csv('/sample-url.csv')

## Array for URL column from CSV file
url_array = df['url']

## Array to store response code 
response_code_result = []

## Loop through array and http request
for x in url_array:
  try:
    response = requests.get(x)
    print(response.status_code)
    response_code_result.append(response.status_code)
  except requests.exceptions.MissingSchema:
    print("error: Invalid URL") 
    response_code_result.append("requests.exceptions.MissingSchema")

## Append result column to existing dataframe 
df['response'] = response_code_result

## "export" Dataframe as CSV
filename = (datetime.today().strftime('%Y%m%d-%H%M') + "-result.csv")
print(filename)
df.to_csv(filename)