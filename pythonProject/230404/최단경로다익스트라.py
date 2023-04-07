def dijkstra(s,e):
    d = adj[s][::]
    v = [0]*N
    v[s]=1

    for _ in range(N-1):
        mn, i_mn = INF, 0
        for j in range(N):
            if v[j] == 0 and mn>d[j]:
                mn, i_mn = d[j],j
        v[i_mn] = 1

        for j in range(N):
            d[j] = min(d[j], d[i_mn]+adj[i_mn][j])
    return d[e]


INF = 50*10
T = int(input())
for test_case in range(1, T + 1):
    N,E = map(int,input().split())
    adj = [[INF]*N for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0

    for _ in range(E):
        s,e,w = map(int, input().split())
        adj[s][e]=w

    ans = dijkstra(0,N-1)
    print(f"#{test_case} {ans}")
