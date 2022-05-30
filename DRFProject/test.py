import requests
BASE_URL='https://api.stackexchange.com/'
ENDPOINT='/2.3/questions?order=desc&sort=activity&site=stackoverflow'
r=requests.get(BASE_URL+ENDPOINT)
data=r.json()
print(data)