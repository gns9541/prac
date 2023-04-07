T = int(input())
for test_case in range(1, T + 1):
    lst = list(input())
    stack = []
    a = 1
    for i in lst:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                a = 0

    if len(stack) != 0 or a == 0:
        print(f"#{test_case}", 0)
    else:
        print(f"#{test_case}", 1)


