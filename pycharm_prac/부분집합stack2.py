T = int(input())
for test_case in range(1, T + 1):
    def f(i, N, s, K):
        global cnt
        if s > K:
            return
        elif s == K:
            cnt += 1
            return
        elif i == N:
            return
        else:
            bit[i] = 1
            f(i+1, N, s+num[i], K)
            bit[i] = 0
            f(i+1, N, s, K)

    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    bit = [0]*N
    cnt = 0
    f(0, N, 0, K)
    print(f"#{test_case} {cnt}")




