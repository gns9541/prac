from collections import deque
T = int(input())
for _ in range(T):
    def bfs():
        while q:
            x, y = q.popleft()
            if visited[x][y] != "FIRE":
                flag = visited[x][y]
            else:
                flag = "FIRE"

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if visited[nx][ny] == -1 and (
                        arr[nx][ny] == "." or arr[nx][ny] == "@"
                    ):
                        if flag == "FIRE":
                            visited[nx][ny] = flag
                        else:
                            visited[nx][ny] = flag + 1
                        q.append((nx, ny))
                else:
                    if flag != "FIRE":
                        return flag + 1

        return "IMPOSSIBLE"

    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    visited = [[-1] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "@":
                visited[i][j] = 0
                start = (i, j)
            elif arr[i][j] == "*":
                visited[i][j] = "FIRE"
                q.append((i, j))

    q.append(start)
    print(bfs())