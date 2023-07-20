import requests
from pprint import pprint as print  # Pretty Print 모듈 사용

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

# API 요청
response = requests.get(API_URL)  # http 메소드인 get 사용

# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
print(response)

# 변환 데이터 출력
print(parsed_data['username'])

dummy_data = []

for i in parsed_data:  # parsed_data라는 리스트에서 반복
    dummy_data.append(i['name'])  # dummy_data 리스트에 'name'이라는 key값을 가진 value 요소 추가

print(dummy_data)