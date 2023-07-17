## For HTTP requerst
# import requests

## For CSV column to array
import pandas as pd
 
df = pd.read_csv('sample-url.csv')

# url = "https://www.google.com"

url_array = df['url']

print(url_array)

# ## HTTP request
# response = requests.get(url)
 
# print(response.status_code)