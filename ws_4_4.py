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

    user_data = {}
    user_data['company'] = parsed_data['company']['name']
    user_data['lat'] = parsed_data['address']['geo']['lat']
    user_data['lng'] = parsed_data['address']['geo']['lng']
    user_data['name'] = parsed_data['username']

    if float(user_data['lat']) < 80 and float(user_data['lng']) > -80:
        dummy_data.append(user_data)

# print(dummy_data)
black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

def create_user(dummy_data):
    censored_user_list = {}

    # dummy_data에서 순회하면서 딕셔너리 요소 하나씩 접근
    for user in dummy_data:
        # user의 회사 정보 확인해서 블랙리스트에 없다면
        if censorship(user) == 1:  # censorship 함수 호출 (True일 경우)
            # censored_user_list 딕셔너리에 company의 value(회사 이름)를 key 값으로 하고 name을 value(user name)로 하는 key-value 쌍 추가
            censored_user_list[user['company']] = [user['name']]  # 요구사항: value는 리스트로 구성한다
    
    return censored_user_list

def censorship(user):
    if user['company'] in black_list:
        print(f"{user['company']}소속의 {user['name']}은/는 등록할 수 없습니다.")
        return False
    else:
        print('이상 없습니다.')
        return True

print(create_user(dummy_data))