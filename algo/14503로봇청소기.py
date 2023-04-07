N,M = map(int, input().split())
r,c,d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)] # 0:청소x 1:벽

di = [-1,0,1,0] # 0:북, 1:동, 2:남, 3:서
dj = [0,1,0,-1]

# k = (k+3) % 4
k = d
i = r
j = c
cnt = 0

while True:
    if cnt == 50:
        break
    if room[i][j] == 0:
        room[i][j] = 2
        cnt+=1
    cnt1 = 0
    for l in range(4):
        li, lj = i+di[l], j+dj[l]
        if room[li][lj] == 0:
            cnt1+=1
    if cnt1 != 0:
        k = (k+3) % 4
        while True:
            ni, nj = i+di[k], j+dj[k]  # 0<=ni<N and 0<=nj<M and room[ni][nj] != 1
            if 0<=ni<N and 0<=nj<M and room[ni][nj] != 1:
                if room[ni][nj] != 0:
                    k = (k+3) % 4
                    
                elif room[ni][nj] == 0:
                    room[ni][nj] = 2
                    cnt += 1
                    i,j = ni,nj
                    break
    elif cnt1 == 0:
        if k == 0:
            k = 2
        elif k == 1:
            k = 3
        elif k == 2:
            k = 0
        elif k == 3:
            k = 1
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<N and 0<=nj<M and room[ni][nj] != 1:
            i,j = ni,nj
    
print(*room, sep="\n")
print(cnt)
            
        






