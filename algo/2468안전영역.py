from copy import deepcopy
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

print(*area, sep="\n")

n = 0
m = 100
for lst in area:
    if max(lst)>n:
        n = max(lst)
for lst in area:
    if min(lst)<n:
        m = min(lst)
print(n,m)

while True:
    arr = deepcopy(area)
    if n == m-1:
        break
    for i in range(N):
        for j in range(N):
            if area[i][j]<=n:
                arr[i][j] = 0
    n-=1
    print(*arr, sep="\n")
    print()

def dfs():
    pass