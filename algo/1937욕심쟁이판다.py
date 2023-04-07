def dfs(i,j):
    global ans
    if v[i][j]:
        return v[i][j]
    else:
        v[i][j] = 1
    for k in range(4):
        ni,nj = i+di[k], j+dj[k]
        if 0<=ni<n and 0<=nj<n and tree[ni][nj]>tree[i][j]:
            v[i][j] = max(v[i][j], dfs(ni,nj)+1)
            
    return v[i][j] 
            
    
n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
ans = 0
v = [[0]*n for _ in range(n)]
di = [1,-1,0,0]
dj = [0,0,1,-1]

for i in range(n):
    for j in range(n):
        # v = [[0]*n for _ in range(n)]
        ans = max(dfs(i,j),ans)

print(ans)

# def dfs(x, y):
#     if dp[x][y]: return dp[x][y] # 이미 한번 왔다간 경로는 그대로 리턴
#     dp[x][y] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
#             dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
#     return dp[x][y]


# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
# dx = [-1, 0, 0, 1]
# dy = [0, -1, 1, 0]
# dp = [[0] * n for _ in range(n)]

# answer = 0
# for i in range(n):
#     for j in range(n):
#         answer = max(answer, dfs(i, j))

# print(answer)

# n = int(input())
# board = [list(map(int,input().split())) for _ in range(n)]
# dp = [[-1]*n for _ in range(n)]
# move = [(0,1),(1,0),(0,-1),(-1,0)]
# ans = 0

# def dfs(x,y):
#     if dp[x][y] == -1:
#         dp[x][y] = 0
        
#         for a,b in move:
#             dx=x+a; dy=y+b
#             if n>dx>=0 and n>dy>=0 and board[dx][dy] > board[x][y]:
#                 dp[x][y] = max(dp[x][y],dfs(dx,dy))
    
#     return dp[x][y]+1

# for i in range(n):
#     for j in range(n):
#         ans = max(ans,dfs(i,j))
            
# print(ans)