C, R = map(int, input().split())
K = int(input())

arr = [[0]*C for _ in range(R)]
# print(*arr, sep='\n')

di = [-1, 0, 1, 0] #시계
dj = [0, 1, 0, -1]


k = 0
cnt = 1
i = R
j = 0
while True:
    if C*R<K:
        print(0)
        break
    if cnt == K+1:
        print(j+1,R-i)
        break
    ni, nj = i+di[k], j+dj[k]
    if 0<=ni<R and 0<=nj<C and arr[ni][nj] == 0:
        arr[ni][nj] = cnt
        cnt += 1  
        i, j = ni, nj
    else:
        k += 1
        if k == 4:
            k = 0

    
