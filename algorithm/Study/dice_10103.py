n = int(input())
chang = sang = 100
for _ in range(n):
    n1, n2 = map(int, input().split())

    if n1 == n2:
        continue
    elif n1 > n2:
        sang -= n1
    else:
        chang -= n2

print(chang)
print(sang)
