# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(word):
    temp = reversed(word)
    rev = "".join(temp)
    return rev

result = reverse_string("Hello, World!")
print(result)