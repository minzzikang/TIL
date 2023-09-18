def get_postfix(n, infix):
    stack = []
    postfix = ''

    for i in range(n):
        # 피연산자면 그대로 출력
        if infix[i] not in ['+', '*']:
            postfix += infix[i]

        # 연산자일 경우
        else:
            # *를 만나면
            if infix[i] == '*':  # 곱하기는 더하기보다
                # 스택이 비어 있지 않고 top 위치 연산자가 더하기가 아니라면 계속 pop해서 계산식에 붙이기
                while stack and stack[-1] != '+':
                    postfix += stack.pop()

                stack.append(infix[i])  # 다 꺼내면 * 스택에 push

            elif infix[i] == '+':
                while stack:  # 스택이 빌 때까지 pop 반복해서 후위 계산식에 붙이기
                    postfix += stack.pop()

                stack.append(infix[i])  # 비어 있으면 스택에 push

    # 스택에 남은 연산자들 pop해서 후위 계산식에 붙이기
    while stack:  # 몇 개 남았는지 모르니까 while문
        postfix += stack.pop()

    return postfix

def get_result(postfix):
    stack = []
    result = 0

    # 후위 계산식 글자 하나씩 확인
    for i in postfix:
        # 피연산자면 바로 stack에 push
        if i not in ['+', '*']:
            stack.append(i)

        # 연산자라면 숫자 2개 꺼내서 계산하기 (계산식이 문자열이므로 형변환 필수!)
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if i == '+':
                result = int(val1) + int(val2)
                stack.append(result)  # 다음 연산때 쓰기 위한 push

            elif i == '*':
                result = int(val1) * int(val2)
                stack.append(result)  # 다음 연산때 쓰기 위한 push

    return stack.pop()  # 마지막에 남은 요소가 계산의 결과

T = 10
for tc in range(1, T+1):
    N = int(input())  # 계산식 길이
    infix = input()  # 중위계산식

    ans = get_postfix(N, infix)

    print(f'#{tc} {get_result(ans)}')