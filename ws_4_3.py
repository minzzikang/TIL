import requests
from pprint import pprint as print  # Pretty Print 모듈 사용

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

# API 요청
response = requests.get(API_URL)  # http 메소드인 get 사용

# JSON -> dict 데이터 변환
parsed_data = response.json()

dummy_data = []

for i in range(10):
    user_data = {}
    user_data['company'] = parsed_data[i]['company']['name']
    user_data['lat'] = parsed_data[i]['address']['geo']['lat']
    user_data['lng'] = parsed_data[i]['address']['geo']['lng']
    user_data['name'] = parsed_data[i]['name']
    if float(parsed_data[i]['address']['geo']['lat']) < 80 and float(parsed_data[i]['address']['geo']['lng']) > -80:
        dummy_data.append(user_data)
    
print(dummy_data)