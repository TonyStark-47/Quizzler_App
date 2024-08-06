import requests


parameters = {
    'amount': 10,
    'type': "boolean",
    # 'category': 18   # for Computer Science related.
}

# using trivial quiz database api
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response_data = response.json()
question_data = response_data['results']
