# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(tup):
  new_tuple = sorted(tup)
  
  return tuple(new_tuple)

result = sort_tuple((5, 2, 8, 1, 3))
print(result)