T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    v1 = [[0]*N for _ in range(N)]
    v2 = [0]*4
    ans = []

    di = [1,1,-1,-1]
    dj = [1,-1,1,-1]

    def dfs(i,j,k,lst):
        global ans,x,y
        
        ni,nj = i+di[k], j+dj[k]
        if ni==x and nj ==y:
            ans.append(lst)
            return
        for p in range(4):
            if 0<=ni<N and 0<=nj<N and v2[p]==0: 
                v2[p] = 1
                v1[i][j] = 1
                dfs(ni,nj,p,lst+[D[i][j]])
                print(*v1,sep="\n")
                print()
                v1[i][j] = 0
           
    for x in range(N):
        for y in range(N):
            for k in range(4):
                dfs(x,y,k,[])

    print(ans)


    # def dfs(i,j,k,add):
    #     global ans,x,y
    #     ni,nj = i+di[k], j+dj[k]
    #     # print(add)
    #     if i==x and j==y:
    #         print(add)
    #         print(*v,sep="\n")
    #         return
    #     # if v[i][j]==1:
    #     #     return
    #     if v[i][j] == 0:
    #         v[i][j] = 1
    #         for p in range(4):
    #             if 0<=ni<N and 0<=nj<N:
    #                 if v[ni][nj] == 0:
    #                     return
    #                 else:
    #                     dfs(ni,nj,p,add+D[i][j])
    #         # v[i][j] = 0

            


    # print(ans)