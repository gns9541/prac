from collections import deque

def bfs(i,j):
    q = deque()
    q.append(s)
    visited[i][j] = 0
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni,nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj]>visited[i][j]+arr[ni][nj]:
                    visited[ni][nj] = visited[i][j]+arr[ni][nj]
                    q.append([ni,nj])

di = [1,-1,0,0]
dj = [0,0,1,-1]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    s = [0,0]
    e=[N-1,N-1]
    visited = [[100*100*9] * N for _ in range(N)]
    bfs(0,0)
    ans = visited[N-1][N-1]
    print(f"{test_case} {ans}")

