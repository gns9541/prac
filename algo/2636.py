def hole():
    for i in range(N):
        for j in range(M):
            if ch[i][j] == 0: # 5, 6
                cnt = 0
                for k in range(0, i):
                    if ch[k][j] ==1:
                        cnt += 1
                        break
                for k in range(i+1, N):
                    if ch[k][j] == 1:
                        cnt += 1
                        break
                for l in range(0, j):
                    if ch[i][l] == 1:
                        cnt += 1
                        break
                for l in range(j+1, M):
                    if ch[i][l] == 1:
                        cnt += 1
                        break
                if cnt == 4:
                    ch[i][j] = 2
N, M = map(int, input().split())

ch = [list(map(int, input().split())) for _ in range(N)]

di = [1,-1,0,0] 
dj = [0,0,1,-1]

time = 0
while True:
    if time ==3:
        break
    ans = 0
    for lst in ch:
        ans += sum(lst)
    if ans == 0:
        break
    hole()
    print(*ch, sep="\n")
    print()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ch[i][j] == 1:
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0<=ni<N and 0<=nj<M:
                        if ch[ni][nj] == 0:
                            ch[i][j] = 3
                            cnt += 1
                            break
    for i in range(N):
        for j in range(M):
            if ch[i][j] == 3 or ch[i][j] == 2:
                ch[i][j] = 0
    print(*ch, sep="\n")
    time += 1

    print(time)
# hole()

