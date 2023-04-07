from copy import deepcopy

# def dfs():
#     cnt = 0
    
#     while True:
#         if cnt == 3:
#             break
#         for a in range(R):
#             for b in range(C):
#                 if maps[a][b] == '*':
#                     for k in range(4):
#                         na,nb = a+di[k], b+dj[k]
#                         if 0<=na<R and 0<=nb<C and maps[na][nb] != 'X' and maps[na][nb] != 'D':
#                             map2[na][nb] = '*'
#         # print(*map2,sep='\n')   
#         for i in range(R):
#             for j in range(C):
#                 if map2[i][j] == 'S':
#                     for k in range(4):
#                         ni,nj = i+di[k], j+dj[k]
#                         if 0<=ni<R and 0<=nj<C and map2[ni][nj] != '*' and map2[ni][nj] != 'X':
#                             map2[ni][nj] = 'S'
                        
#                             # dfs(ni,nj,t+1)
#                             # map2[ni][nj] = '.'
#         for i in range(R):
#             for j in range(C):
#                 if maps[i][j] == 'S':
#                     for k in range(4):
#                         ni,nj = i+di[k], j+dj[k]
#                         if 0<=ni<R and 0<=nj<C and maps[ni][nj] == 'D':
#                             print(cnt+1)
#                             return
                
#         cnt += 1
#         print(*map2,sep='\n')
#         print()
#         maps = deepcopy(map2)



R,C = map(int, input().split())
maps = [list(map(str,input())) for _ in range(R)]

di = [1,-1,0,0]
dj = [0,0,1,-1]
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'D':
            x=i
            y=j
        if maps[i][j] == 'S':
            si=i
            sj=j
map2 = deepcopy(maps)
cnt = 0
map2 = deepcopy(maps)
while True:
    if cnt == 3:
        break
    for a in range(R):
        for b in range(C):
            if maps[a][b] == '*':
                for k in range(4):
                    na,nb = a+di[k], b+dj[k]
                    if 0<=na<R and 0<=nb<C and maps[na][nb] != 'X' and maps[na][nb] != 'D':
                        map2[na][nb] = '*'
    # print(*map2,sep='\n')   
    for i in range(R):
        for j in range(C):
            if map2[i][j] == 'S':
                for k in range(4):
                    ni,nj = i+di[k], j+dj[k]
                    if 0<=ni<R and 0<=nj<C and map2[ni][nj] != '*' and map2[ni][nj] != 'X':
                        map2[ni][nj] = 'S'
                    
                        # dfs(ni,nj,t+1)
                        # map2[ni][nj] = '.'
    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'S':
                for k in range(4):
                    ni,nj = i+di[k], j+dj[k]
                    if 0<=ni<R and 0<=nj<C and maps[ni][nj] == 'D':
                        break
            break
    cnt += 1
    # print(*map2,sep='\n')
    # print()
    maps = deepcopy(map2)
print(cnt+1)

