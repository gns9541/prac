N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di,dj = [-1,1,0,0,1],[0,0,1,-1,1] # 상 하 우 좌 대
ans = []

def dfs():
    for k in range(N):
        for l in range(M):
            if t1(l,k):
                ans.append(t1(k,l))
            if t2(l,k):
                ans.append(t2(k,l))
            if t3(l,k):
                ans.append(t3(k,l))
            if t4(l,k):
                ans.append(t4(k,l))
            if t5(l,k):
                ans.append(t5(k,l))
            

def t1(i,j):
    fin = []
    for k in range(0,4):
        ni,nj = i+k*di[2],j+k*dj[2]
        if 0<=ni<N and 0<=nj<M:
            fin.append(arr[ni][nj])
    
    if len(fin)==4:
        print(fin)
        return sum(fin)
    else:
        return 0
    
    

def t2(i,j):
    fin = []
    fin.append(arr[i][j])
    for k in range(4):
        if k != 0:
            ni,nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<M:
                fin.append(arr[ni][nj])
            
    if len(fin)==4:
        print(fin)
        return sum(fin)
    else:
        return 0
    

def t3(i,j):
    fin = []
    fin.append(arr[i][j])
    for k in range(5):
        if k == 1 or 2 or 4:
            ni,nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<M:
                fin.append(arr[ni][nj])
            
    if len(fin)==4:
        return sum(fin)
    else:
        return 0
   
    
def t4(i,j):
    fin = []
    for k in range(0,3):
        ni,nj = i+k*di[1],j+k*dj[1]
        if 0<=ni<N and 0<=nj<M:
            fin.append(arr[ni][nj])
        
    if 0<=i+2<N and 0<=nj+1<M:
        fin.append(arr[i+2][j+1])
    if len(fin)==4:
        return sum(fin)
    else:
        return 0
  
def t5(i,j):
    fin = []
    fin.append(arr[i][j])
    for k in range(5):
        if k == 1 or 4:
            ni,nj = i+di[k],j+dj[k]
            if 0<=ni<N and 0<=nj<M:
                fin.append(arr[ni][nj])
            
    if 0<=i+2<N and 0<=nj+1<M:
        fin.append(arr[i+2][j+1])
    if len(fin)==4:
        return sum(fin)
    else:
        return 0
  
dfs() 
print(max(ans))        
# def t2(i,j):
#     for k in range(1,5):
#         ni,nj = i+k*di[2],j+k*dj[2]
#         if 0<ni<=N and 0<nj<=M:
#             arr[ni][nj] == 1
#         else:
#             return
# def t3(i,j):
#     for k in range(1,5):
#         ni,nj = i+k*di[2],j+k*dj[2]
#         if 0<ni<=N and 0<nj<=M:
#             arr[ni][nj] == 1
#         else:
#             return
# def t4(i,j):
#     for k in range(1,5):
#         ni,nj = i+k*di[2],j+k*dj[2]
#         if 0<ni<=N and 0<nj<=M:
#             arr[ni][nj] == 1
#         else:
#             return
# def t5(i,j):
#     for k in range(1,5):
#         ni,nj = i+k*di[2],j+k*dj[2]
#         if 0<ni<=N and 0<nj<=M:
#             arr[ni][nj] == 1
#         else:
#             return


