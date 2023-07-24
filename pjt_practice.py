import json  # 내장된 json 모듈(라이브러리)

# 여러 개의 문자열 쓸때 '''로 감싸주기
json_data = '''
{
    "name": "김싸피",
    "age": 28,
    "hobbies": [
        "공부하기",
        "복습하기"
    ]
}
'''

data = json.loads(json_data)  # json형식의 문자열을 파싱하여 dict로 변환  / 파싱: 원하는 데이터 형태로 변환

# JSON 데이터에서 원하는 데이터만 가져오기
name = data.get('name')

print(name)

