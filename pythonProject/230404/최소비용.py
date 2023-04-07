from collections import deque

def bfs(i,j):
    q = deque()
    q.append(s)
    visited[i][j] = 0
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni,nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                if arr[ni][nj]>arr[i][j]:
                    visited[ni][nj]=visited[ni][nj]+arr[ni][nj]-arr[i][j]
                q.append([ni, nj])

            if 0<=ni<N and 0<=nj<N and visited[ni][nj] != 0:
                if arr[ni][nj] > arr[i][j]:
                    if visited[i][j] + 1+ arr[ni][nj]-arr[i][j] < visited[ni][nj]:
                        visited[ni][nj] = visited[i][j] + 1+arr[ni][nj]-arr[i][j]
                        q.append([ni, nj])
                else:
                    if visited[i][j] + 1 < visited[ni][nj]:
                        visited[ni][nj] = visited[i][j] + 1
                        q.append([ni, nj])


di = [1,-1,0,0]
dj = [0,0,1,-1]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    s = [0,0]
    e=[N-1,N-1]
    visited = [[0] * N for _ in range(N)]
    bfs(0,0)
    ans = visited[N-1][N-1]
    # print(*visited,sep="\n")
    print(f"#{test_case} {ans}")