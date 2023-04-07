T = int(input())
for test_case in range(1, T + 1):
    def f(i, N, s, K):
        global cnt
        if s > K:
            return
        elif s == K:
            if bit.count(1) == N:
                cnt += 1
                print(bit)
            else:
                return
            return
        elif i == 12:
            return
        else:
            bit[i] = 1
            f(i+1, N, s+A[i], K)
            bit[i] = 0
            f(i+1, N, s, K)

    N, K = map(int, input().split())
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    bit = [0]*12
    cnt = 0
    f(0, N, 0, K)
    print(f"#{test_case} {cnt}")
