def cal(N, M):
    if M <= 1:
        return N
    else:
        return N*cal(N, M-1)


for test_case in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    ans = cal(N,M)
    print(f"#{T} {ans}")

################################
# 곱하는 횟수가 M이 될때 종료하는 식으로도 짤 수 있음


