def bfs(v, N):
    # visited 생성
    visited = [0]*(N+1)
    # 큐 생성
    # 시작점 인큐
    q = [v]
    #시작점 인큐표시
    visited[v] = 1
    ans = []
    while q:       # 큐가 비어있지 않으면
        t = q.pop(0) # 디큐
        ans.append(t) # t에서 처리할 일
        for v in adjL[t]:  # t에 인접이고 방문한 적 없는 v
            if visited[v] == 0:
                # v 인큐하고 표시
                q.append(v)
                visited[v] = visited[t]+1
    
    return ans

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    arr = []
    for _ in range(E):
        arr.append(list(map(int, input().split())))
    arr = sum(arr, [])
    # print(arr)
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)
    # bfs(1, V)
    print(f"#{test_case}", *bfs(1, V) ) 

    # ans = bfs(1, V) # 시작정점 1, 
