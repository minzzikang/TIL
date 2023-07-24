import requests
from pprint import pprint as print  # Pretty Print 모듈 사용

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []

for num in range(1, 11):
    NEW_URL = API_URL + str(num)

    # API 요청
    response = requests.get(NEW_URL)

    # JSON -> dict 데이터 변환
    parsed_data = response.json()

info_dict = {}
info_dict['company'] = parsed_data['company']['name']
info_dict['lat'] = parsed_data['address']['geo']['lat']
info_dict['lng'] = parsed_data['address']['geo']['lng']
info_dict['name'] = parsed_data['username']

if float(parsed_data['address']['geo']['lat']) < 80 and float(parsed_data['address']['geo']['lng']) > -80:
    dummy_data.append(info_dict)

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

def censorship(user):
    if user['company']['name'] in black_list:
        print(f"{user['company']['name']}소속의 {user['name']}은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다.')
        return True

def create_user(input_list):
    censored_user_list = {}

    for user in input_list:
        if censorship(user) == 1:
            censored_user_list[user['company']] = [user['name']]
    
    return censored_user_list

print(create_user(dummy_data))