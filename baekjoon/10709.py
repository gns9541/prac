H, W = map(int, input().split())
cloud = [list(input()) for _ in range(H)]
area = [list([-1]*W) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if cloud[i][j] == 'c':
            area[i][j] = 0
        else:
            for k in range(j-1,-1,-1):
                if cloud[i][k] == 'c':
                    area[i][j] = j-k
                    break
for i in area:
    print(*i)
