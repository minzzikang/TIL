# 균형잡힌 세상
while True:
    word = input()
    stack = []

    if word == '.':
        break

    for w in word:
        if w == '(' or w == '[':
            stack.append(w)

        elif w == ']':
            if stack and stack[-1] != '(':
                stack.pop()  # 짝 맞으면 pop

            else:
                stack.append(w)
                break

        elif w == ')':
            if stack and stack[-1] != '[':
                stack.pop()

            else:
                stack.append(w)
                break

    if stack:
        print('no')
    else:
        print('yes')
