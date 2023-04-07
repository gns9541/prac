# def bfs():
import copy
from collections import deque
# 빙산 탐색 함수
def bfs(i,j):
    visited = [[0]*M for _ in range(N)]
    q = deque([[i,j]])
    print(q)
    visited[i][j] = True
    # print(visited)
    for p in range(len(lst)):
        while q:
            if len(q) == len(lst):
                break
            i = lst[p][0]
            j = lst[p][1]
            while True:
                ni,nj = i, j
                for k in range(4):
                    ni, nj = ni+di[k], nj+dj[k] 
                    if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and ice[ni][nj] != 0:
                        visited[ni][nj] = True
                        q.append([ni,nj])
                        print(q)

    return print(*visited,q, sep="\n") 
    


N,M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*M for _ in range(N)]

di = [-1, 1, 0, 0] # 상 하 좌 우
dj = [0, 0, -1, 1]



t=0
while True:
    new = copy.deepcopy(arr)
    if t == 2:
        break
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0<=ni<N and 0<=nj<M and ice[ni][nj] == 0:
                        cnt += 1
                if ice[i][j] - cnt >= 0:
                    new[i][j] = ice[i][j]
                    new[i][j] = new[i][j] - cnt
                else:
                    new[i][j] = 0
    lst = []
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                lst.append([i,j])

    ice = copy.deepcopy(new)
    t+=1
    bfs(lst[0][0],lst[0][1])
    print(*new, sep="\n")
    print()

# visited = [[0]*M for _ in range(N)]

