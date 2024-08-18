import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    "userId": 1,
    "title": 'John',
    "body": 'This is a sentence.',
}

headers = {
    'Content-type': 'application/json;charset=UTF-8'
}

response = requests.post(url, headers=headers, json=data)

# Debugging output
print(f'Response Content: {response.json()}')
