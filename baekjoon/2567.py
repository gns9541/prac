N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]+[0]*102+[0] for _ in range(104)]
# print(*arr, sep="\n")
for k in range(len(lst)):
    for i in range(lst[k][1], lst[k][1]+10):
        for j in range(lst[k][0], lst[k][0]+10):
            arr[i][j] = 1

di = [0, 0, -1, 1] # 좌 우 상 하
dj = [-1, 1, 0, 0]
# print(*arr, sep="\n")

cnt = 0
for i in range(0,102):
    for j in range(0,102):
        for k in range(4):
            if arr[i][j] == 0:
                if arr[i+di[k]][j+dj[k]]==1:
                    cnt += 1
                
print(cnt)