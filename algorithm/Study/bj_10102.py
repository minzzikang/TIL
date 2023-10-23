v = int(input())
vote = list(input())
a_cnt = b_cnt = 0

for i in range(v):
    if vote[i] == 'A':
        a_cnt += 1
    else:
        b_cnt += 1

if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
else:
    print('Tie')