from copy import deepcopy

R,C,M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(M)]
# f = [[1]*(C+1)]+[[1]+[0]*C for _ in range(R)] 
# v = [[1]*(C+1)]+[[1]+[0]*C for _ in range(R)]
# print(*f, sep="\n")
di = [0,-1,1,0,0] # 상 하 오 왼 1,2,3,4
dj = [0,0,0,1,-1]

# for lst in shark:
#     r = lst[0] #위치
#     c = lst[1]
#     s = lst[2] #속력
#     d = lst[3] #이동방향
#     z = lst[4] #크기
    
#     f[r][c] = lst

# print(*f, sep="\n")
# print()

p = 1
cnt = 1
while True:
    f = [[1]*(C+1)]+[[1]+[0]*C for _ in range(R)] 
    for lst in shark:
        r = lst[0] #위치
        c = lst[1]
        s = lst[2] #속력
        d = lst[3] #이동방향
        z = lst[4] #크기
    
        f[r][c] = lst
    v = deepcopy(f)
    if p == 3:
        break
    for i in range(R+1):
        for j in range(C+1):
            if f[i][j] != 0 and f[i][j] != 1:
                lst = f[i][j] 
                if lst[1] == p:
                    f[i][j]=0
                    cnt+=1
                    break
        break
    print(*f, sep="\n")           # print(lst)
    for i in range(R+1):
        for j in range(C+1):
            if f[i][j] != 0 and f[i][j] != 1:
                lst = f[i][j] 
                r = lst[0] #위치
                c = lst[1]
                d = lst[3]
                s = lst[2]
                ni,nj = r+s*di[d],c+s*dj[d]
                if 1<=ni<R+1 and 1<=nj<C+1 and v[ni][nj] == 0:
                    # print(lst)
                    v[ni][nj] = lst
                if ni<1 or ni>=R+1 or nj<1 or nj>=C+1:
                    t = s
                    cnt = 2
                    while True:
                        if t == 0:
                            if v[r][c] == 0:
                                v[r][c] = lst
                                break
                            else:
                                v[r][c] += lst
                                break
                        ki,kj = r+(-1)**cnt*di[d],c+(-1)**cnt*dj[d]
                        if 1<=ki<R+1 and 1<=kj<C+1:
                            r,c = ki,kj
                        elif ki == R+1 or kj == C+1 or ki == 0 or kj == 0:
                            cnt+=1
                            ki,kj = r+(-1)**cnt*di[d],c+(-1)**cnt*dj[d]
                            r,c = ki,kj
                        t-=1
                
                # elif 1<=ni<R+1 and 1<=nj<C+1 and v[ni][nj] != 0:
                #     v[ni][nj] += lst
    lst = deepcopy(v)
    p+=1                

print(*v, sep="\n")
