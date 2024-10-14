N = int(input())
words = []
for _ in range(N):
    s = input()
    words.append(s)

cnt = 0
for word in words:
    check = []
    valid = True
    check.append(word[0])
    for i in range(1, len(word)):
        if word[i] not in check:
            check.append(word[i])
        else:
            if word[i] != word[i-1]:
                valid = False
                break
    if valid:
        cnt += 1

print(cnt)