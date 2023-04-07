from copy import deepcopy

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(K)]

    arr = [[0]*N for _ in range(N)]

    di = [0, -1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, 0, -1, 1]

    for k in range(K):
        i, j = lst[k][0], lst[k][1]
        arr[i][j] = [lst[k][2],lst[k][3]]

    while M>0:
        arr2 = [[0]*N for _ in range(N)]
        for k in range(len(lst)):
            i, j, d = lst[k][0], lst[k][1], lst[k][3]
            ni,nj = i+di[d], j+dj[d]
            if ni==0 or ni==N-1 or nj==0 or nj==N-1:
                arr2[ni][nj] = [arr[i][j][0]//2,arr[i][j][1]]
                if arr2[ni][nj][1] == 1:
                    arr2[ni][nj][1] = 2
                elif arr2[ni][nj][1] == 2:
                    arr2[ni][nj][1] = 1
                elif arr2[ni][nj][1] == 3:
                    arr2[ni][nj][1] = 4
                elif arr2[ni][nj][1] == 4:
                    arr2[ni][nj][1] = 3
            else:
                if arr2[ni][nj] != 0:
                    arr2[ni][nj] += arr[i][j]
                else:
                    arr2[ni][nj] = arr[i][j]
            arr[i][j] = 0

        for i in range(N):
            for j in range(N):
                if arr2[i][j] != 0:
                    if len(arr2[i][j])>2:
                        new = [0,0]
                        l = arr2[i][j]
                        for k in range(len(l)):
                            if k%2 == 0:
                                new[0] += l[k]
                                new[1] = max(l[k],new[1])
                        for k in range(len(l)):
                            if k % 2 == 0:
                                if new[1] == l[k]:
                                    new[1] = l[k+1]
                        arr2[i][j] = new
        arr=arr2
        M-=1
        lst = []
        for i in range(N):
            for j in range(N):
                if arr2[i][j] != 0:
                    lst.append([i,j,arr[i][j][0],arr[i][j][1]])

    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                ans+=arr[i][j][0]
    print(f"#{test_case} {ans}")






