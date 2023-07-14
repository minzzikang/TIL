import random
GAME = ["가위", "바위", "보"]

user = input("가위/바위/보 중에 입력하세요: ")

print(user)

com = random.choice(GAME)

if user == "가위" and com == "바위":
    print("승자 : computer")
    print(f"내가 {user}을 내고 컴퓨터가 {com}을 내서 패배하였습니다.")
elif user == "가위" and com == "보":
    print("승자 : user")
    print(f"내가 {user}을 내고 컴퓨터가 {com}을 내서 승리하였습니다.")
elif user == "바위" and com == "보":
    print("승자 : computer")
    print(f"내가 {user}을 내고 컴퓨터가 {com}을 내서 패배하였습니다.")
elif user == "바위" and com == "가위":
    print("승자 : user")
    print(f"내가 {user}을 내고 컴퓨터가 {com}을 내서 승리하였습니다.")
elif user == "보" and com == "가위":
    print("승자 : computer")
    print(f"내가 {user}을 내고 컴퓨터가 {com}을 내서 패배하였습니다.")
elif user == "보" and com == "바위":
    print("승자 : user")
    print(f"내가 {user}을 내고 컴퓨터가 {com}을 내서 승리하였습니다.")
else:
    print(f"내가 {user}을 내고 컴퓨터가 {com}을 내서 비겼습니다.")
    