def bfs(vi, vj, N):
    visited = [[0]*N for _ in range(N)]
    q = [[vi,vj]]
    visited[vi][vj] = 1
    ans = []
    while q:
        t = q.pop(0)
        ans.append(t)
        for v in miro[t[0]][t[1]]:
            print(v)







T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]

    print(*miro, sep="\n")

    vi = vj = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                vi, vj = i, j
    adj = [[] for _ in range(N)]

    print(vi, vj)
    bfs(vi, vj, N)
