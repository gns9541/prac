def dfs(n,add):
    global ans
    if add<=ans:  
        return

    if n == N:
        ans = max(add,ans)
        return
    
    
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, add*P[n][j]/100)
            v[j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    ans = 0

    dfs(0,1)
    print(f"#{test_case} {round(ans*100,6):.6f}")