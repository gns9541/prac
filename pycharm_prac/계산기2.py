# 숫자면 스택에 푸쉬
# 숫자 아니면 두개 팝해서 연산하고 푸쉬
# 괄호가 있는 경우 괄호가 열리면 무조건 푸쉬해준다 -> 새로운 스택 느낌
# 우선순위 정해주기

pri = {"+":1, "*":2}
T = 1
for test_case in range(1, T + 1):
    N = int(input())
    st = input()
    equ = ""
    stk = []
    # 후위표기식 변환
    for ch in st:
        if ch.isdigit():
            equ += ch
        else:
            while stk and pri[ch] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(ch)
    while stk:
        equ += stk.pop()

    # 후위표기식 연산
    ans = 0
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            if len(stk) >= 2:
                if ch == "+":
                    stk.append(stk.pop()+stk.pop())
                elif ch == "*":
                    stk.append(stk.pop()*stk.pop())
                else:
                    ans = "error"
                    break
            else:
                ans = "error"
                break
    if ans != "error":
        ans = stk.pop()

    print(f"#{test_case} {ans}")











