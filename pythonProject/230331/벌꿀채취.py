T = int(input())
for test_case in range(1, T + 1):
    N,M,C = map(int,input().split())
    H = [list(map(int,input().split())) for _ in range(N)]
    # v = [[0]*N for _ in range(N)]
    ans = []
    ans2 = []
    def f(i,j):
        lst = []
        lst2 = []
        for k in range(M):
            nj = j+k
            if 0<=i<N and 0<=nj<N and v[i][nj]==0:
                v[i][nj] = 1
                lst.append(H[i][nj])
                lst2.append([i,j])
        if len(lst)==M:
            ans.append(lst)
        ans2.append(lst2)
        return lst


    
    def dfs(i,j,cnt):
        if cnt == 2:
            return
        f(i,j)
        dfs(i,j,cnt+1)

        

    for i in range(N):
        for j in range(N):
            v = [[0]*N for _ in range(N)]
            dfs(i,j,0)
    
    print(ans)
    print(ans2)
    # print(*v,sep="\n")