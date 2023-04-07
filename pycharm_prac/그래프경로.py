def dfs(s):
    stk = []

    while True:
        for e in adj[s]:    #s에 연결된 노드 순서대로
            if v[e] == 0:   #미방문일때
                stk.append(s)

                s = e
                v[s] = 1
                break
            print(v)
        else:          #연결 x
            if stk:
                s = stk.pop()
            else:
                break

T = int(input())
for test_case in range(1, T + 1):
    V,E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
    print(*adj, sep="\n")
    S, G = map(int, input().split())
    v = [0]*(V+1)
    dfs(S) # 끝까지 실행

    print(f"#{test_case} {v[G]}")

