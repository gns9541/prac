pri = {"+":1, "*":2, "(":0}

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    st = input()
    stack = []
    eq = ""
    # 후위 표기식으로
    # 우선순위..? 괄호
    for i in st:
        if i.isdigit():
            eq+=i

        else:
            if i == '(':
                stack.append()


