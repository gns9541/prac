def dfs(v,k):
    global ans
    visited[v] = 1
    ans.append(v)
    for w in adjL[v]:
        if visited[w] == 0:
            dfs(w,k)


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr = sum(arr,[])
    # print(arr)
    adjL = [[] * (V + 1) for _ in range(V + 1)]
    visited = [0]*(V+1)
    ans = []
    for i in range(E):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    dfs(1,V)
    print(f"#{test_case}", *ans)

