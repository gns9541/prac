# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs1(v,k): # 재귀, 중복없이 빠짐없이 방문, i번 정점, 정점개수 k
    visited[v] = 1
    print(v)
    for w in adjL[v]:     ## 인접 리스트 사용
        if visited[w] == 0:
            dfs1(w,k)
    # for w in range(1,k+1):   # 인접 행렬 사용
    #     if adjM[v][w] == 1 and visited[w] == 0:
    #         dfs1(w,k)

def dfs2(s,k): # 반복
    stack = []
    visited = [0]*(k+1) 
    v = s
    while True:
        if visited[v] == 0:
            print(v)
            visited[v] = 1
        for w in range(1, k+1):
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
                break
        else: # 더이상 인접인 정점이 없음
            if stack: # 스택이 비어있지 얺으면
                v = stack.pop()
            else: # 비어있으면
                break

def dfs3(v,k,g):
    global cnt
    if v==g:
        cnt += 1
    else:
        visited[v] = 1
        for w in adjL[v]:     ## 인접 리스트 사용
            if visited[w] == 0:
                dfs3(w,k,g)
        visited[v] = 0
        # for w in range(1,k+1):   # 인접 행렬 사용
        #     if adjM[v][w] == 1 and visited[w] == 0:
        #         dfs1(w,k)


V,E = map(int,input().split())
arr = list(map(int,input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[]*(V+1) for _ in range(V+1)]
for i in range(E):
    n1,n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1       # 인접행렬
    adjM[n2][n1] = 1

    adjL[n1].append(n2)    # 인접 리스트
    adjL[n2].append(n1)

print(*adjM,sep="\n")
print()
print(adjL,sep="\n")

visited = [0]*(V+1)
cnt = 0
# dfs1(1,V)
# dfs2(1,V)
dfs3(1,V,7)
print(cnt)