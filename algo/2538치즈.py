from copy import deepcopy

N,M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
# print(*cheese, sep="\n")
di = [1,-1,0,0]
dj = [0,0,1,-1]
c = deepcopy(cheese)

# def f():
#     for i in range(N):
#         for j in range(M):
#             if cheese[i][j] == 0:
#                 cnt = 0
#                 for k in range(N):
#                     if cheese[k][j] == 1 and k < i:
#                         cnt += 1
#                     if cheese[k][j] == 1 and k > i:
#                         cnt += 1
#                 if cnt >= 2:
#                     cnt1= 0
#                     for l in range(M):
#                         if cheese[i][l] == 1 and l < j:
#                             cnt1 += 1
#                         if cheese[i][l] == 1 and l > j:
#                             cnt1 += 1
#                     if cnt1>=2:
#                         cheese[i][j] == 2


# t=0
# while True:
#     c = deepcopy(cheese)
#     cnt = 0
#     for lst in c:
#         if sum(lst) != 0:
#             cnt += 1
#     if cnt == 0:
#         break
#     for i in range(N):
#         for j in range(M):
#             if cheese[i][j] == 1:
#                 cnt = 0
#                 for k in range(4):
#                     ni, nj = i+di[k], j + dj[k]
#                     if 0<=ni<N and 0<=nj<M and cheese[ni][nj] == 0:
#                         cnt +=1
#                 if cnt >=2:
#                     c[i][j] = 0
#     cheese = c
#     f()
#     t += 1
#     print(*c, sep="\n")
#     print()
# print(t)

def f():
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 0:
                cnt = 0
                for k in range(N):
                    if cheese[k][j] == 1 and k < i:
                        cnt += 1
                        
                    if cheese[k][j] == 1 and k > i:
                        cnt += 1
                        
                if cnt >= 2:
                    cnt1= 0
                    for l in range(M):
                        if cheese[i][l] == 1 and l < j:
                            cnt1 += 1
                        if cheese[i][l] == 1 and l > j:
                            cnt1 += 1
                    if cnt1>=2:
                        cheese[i][j] = 2
    print(*cheese, sep="\n")
f()
