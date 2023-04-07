from itertools import combinations
from copy import deepcopy
from collections import deque

N,M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

candidates = [] # 벽의 후보군 이중 3개 뽑아 1로 바꿔줌
virus = []
wall = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            candidates.append((i,j))
        elif lst[i][j] == 2:
            virus.append((i,j))
        elif lst[i][j] == 1:
            wall += 1

tmp_walls = combinations(candidates,3)

ans = N*M
for tmp_wall in tmp_walls:
    infection = 0 # 확산된 바이러스
    flag = 0
    grid = deepcopy(lst)
    for i,j in tmp_wall:      # 벽 세우고
        grid[i][j] = 1
    
    now_virus = deque(virus)  # 바이러스 확산시키기
    while now_virus:
        x,y = now_virus.popleft()

        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if 0<=nx<N and 0<=ny<M:
                if grid[nx][ny] == 0:
                    now_virus.append((nx,ny))
                    grid[nx][ny] = 2
                    infection += 1
                    if infection>ans:
                        flag = 1
                        break
        if flag:
            break
    ans = min(ans,infection)

# 남은 0의 개수
print(N*M - len(virus) - wall -ans - 3)







