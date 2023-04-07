for test_case in range(1, 11):
    N, num = input().split()
    num = list(map(int, num))
    N = int(N)
    i = 0
    while i < N:
        # if i == N:
        #     break
        if num[i] != num[i + 1]:
            i += 1
            if i == len(num)-1:
                break
        elif num[i] == num[i + 1]:
            num.pop(i)
            num.pop(i)
            i = 0
    num = "".join(map(str,num))
    print(f"#{test_case} {num}")


# 스택으로도 풀어보기
# T = 10
# for test_case in range(1, T + 1):
#     _ , st = input().split()
#     stk = []
#     for ch in st:
#         if stk and ch==stk[-1]: # 같은 문자인 경우 스택에서 제거
#             stk.pop()
#         else:                   # 같지 않은 경우 스택에 보관
#             stk.append(ch)
#     print(f'#{test_case} {"".join(stk)}')
#10 1238099084




