# book.py
number_of_book = 100

def decrease_book(n):  # 대여하는 책의 수 : n
    global number_of_book
    number_of_book -= n  # 넘겨받은 매개변수만큼 감소
    print(f'남은 책의 수 : {number_of_book}')