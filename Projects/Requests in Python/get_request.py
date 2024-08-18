import requests

url = 'https://jsonplaceholder.typicode.com/posts'

r = requests.get(url)
print(r.text)
