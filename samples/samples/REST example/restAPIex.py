import requests
import json
#REST API example
response = requests.get(
    'http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else: 
        print("skipped")
    print()

#RERFERENCES:
# https://www.youtube.com/watch?v=qbLc5a9jdXo
# https://api.stackexchange.com/docs/comments
# https://api.stackexchange.com/2.3/comments?order=desc&sort=creation&site=stackoverflow