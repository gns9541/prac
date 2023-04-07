N,M,x,y,K = map(int,input().split())
dc = [list(map(int,input().split())) for _ in range(N)]
order = list(map(int,input().split())) # 동:1 서:2 남:4 북:3
dice = [0]*7
maps = [[0]*M for _ in range(N)]

di = [0,0,0,-1,1] 
dj = [0,1,-1,0,0]

de = [6,3,1,4]
dw = [6,4,1,3]
ds = [6,5,1,2]
dn = [6,2,1,5]
dd=[[0],[6,3,1,4],[6,4,1,3],[6,2,1,5],[6,5,1,2]]

def e():
    dice[1] = dice[]
def w():
    pass
def s():
    pass
def n():
    pass



i=x
j=y
n = 1
for k in order:
    ni, nj = i+di[k], j+dj[k]
    if n == 4:
        n = 0
    if 0<=ni<N and 0<=nj<M:
        if dc[ni][nj] != 0: #and dice[dd[k][n]] == 0:
            dice[dd[k][n]] = dc[ni][nj]
            dc[ni][nj] = 0
            i,j = ni,nj
            n+=1
        elif dc[ni][nj] == 0 and dice[dd[k][n]] != 0:
            dc[ni][nj] = dice[dd[k][n]]
            i,j = ni,nj
            n+=1
        # if dd[k][n] == 1:
        #     print(dice[6])
        # if dd[k][n] == 2:
        #     print(dice[5])
        # if dd[k][n] == 3:
        #     print(dice[4])
        # if dd[k][n] == 4:
        #     print(dice[3])
        # if dd[k][n] == 5:
        #     print(dice[2])
        # if dd[k][n] == 6:
        #     print(dice[1])
    else:pass
    

    print(dice)
    print(*dc,sep="\n")
    print()

