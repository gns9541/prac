T = int(input())
for test_case in range(1, T + 1):
    def dfs(n):
        global ans
        if n == N:  # 종료조건
            ans += 1
            return
        # 하부함수 호출
        for j in range(N):
            if v[j] == v1[n + j] == v2[n - j] == 0:
                # visited 표시
                v[j] = v1[n + j] = v2[n - j] = 1
                dfs(n + 1)
                # visited 표시헤제
                v[j] = v1[n + j] = v2[n - j] = 0


    N = int(input())
    ans = 0
    v = [0] * N
    v1 = [0] * (2 * N)
    v2 = [0] * (2 * N)
    dfs(0)
    print(f"#{test_case} {ans}")