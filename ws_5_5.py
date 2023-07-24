# ws_5_5.py

# 아래 함수를 수정하시오.
# remove 사용
'''
def even_elements(num_li):
    for i in num_li[:]:  
        if i % 2 != 0:
            num_li.remove(i)
    return num_li
'''
# pop만 사용

def even_elements(num_li):
    for i in num_li[:]:  
        if i % 2 != 0:
            num_li.pop(num_li.index(i))
    return num_li


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
