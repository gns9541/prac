def bfs(v,N):
    visited = [0]*(N+1)
    q = [v]
    visited[v] = 1
    ans = []
    while q:
        t = q.pop(0)
        ans.append(t)
        for v in adjL[t]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = visited[t]+1
    return ans


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr = sum(arr,[])
    # print(arr)
    adjL = [[] for _ in range(V+1)]

    for i in range(E):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    print(f"#{test_case}", *bfs(1,V))
