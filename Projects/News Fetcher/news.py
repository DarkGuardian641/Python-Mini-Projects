import requests
import json

query = input("What type of News are you interested in? ")

url = f'https://newsapi.org/v2/everything?q={query}&apiKey=00b43b31f33e480cad9c7f9e48b6b518'

r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    news = r.json()

for article in news['articles']:
    print('\n')
    print('Title: ', article['title'])
    print('Description: ', article['description'])
    print('Check out the News here: ',article['url'])
    print('\n')
    print('-----------------------------------------------------------------')
