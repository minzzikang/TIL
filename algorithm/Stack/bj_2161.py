N = int(input())

cards = []
ans = []

for i in range(1, N+1):
    cards.append(i)

while len(cards) != 1:
    ans.append(cards.pop(0))
    cards.append(cards.pop(0))


for j in ans:
    print(j, end=" ")
print(cards[0])