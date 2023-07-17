## For HTTP requerst
import requests
## For CSV column to array
import pandas as pd
 
## "import" the CSV file
df = pd.read_csv('sample-url.csv')

## Array for URL column from CSV file
url_array = df['url']

## Array to store response code 
response_code_result = []

## Loop through array and http request test
for x in url_array:
  try:
    response = requests.get(x)
    print(response.status_code)
    response_code_result.append(response)
  except requests.exceptions.MissingSchema:
    print("error: Invalid URL") 
    response_code_result.append("requests.exceptions.MissingSchema")

print("result array: ", response_code_result)