T = int(input())
for test_case in range(1, T + 1):
    lst = list(input().split())
    stack = []
    a = 1
    for i in lst:
        for j in i:
            if j == '(':
                stack.append(j)
            elif j == '{':
                stack.append(j)
            elif j == '}':
                if len(stack) != 0:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        a = 0
                else:
                    a = 0
            elif j == ')':
                if len(stack) != 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        a = 0
                else:
                    a = 0
            print(stack)
    if len(stack) != 0 or a == 0:
        print(f"#{test_case}", 0)
    else:
        print(f"#{test_case}", 1)
