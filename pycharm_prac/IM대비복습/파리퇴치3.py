T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(*arr, sep="\n")
    di = [0, 0, -1, 1] # 좌 우 상 하
    dj = [-1, 1, 0, 0]
    dk = [-1, 1, 1, -1] # 우 좌
    dl = [1, 1, -1, -1]

    p1 = []
    p2 = []
    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]
            cnt2 = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni, nj = i + l*di[k], j + l*dj[k]
                    si, sj = i + l * dk[k], j + l*dl[k]
                    if 0<= ni<N and 0<=nj<N:
                        cnt1 += arr[ni][nj]
                    if 0<= si<N and 0<=sj<N:
                        cnt2 += arr[si][sj]
            p1.append(cnt1)
            p2.append(cnt2)
    if max(p1) >= max(p2):
        print(f"#{test} {max(p1)}")
    else:
        print(f"#{test} {max(p2)}")
    # print(max(p1))
    # print(max(p2))
    # print()
    # print(p1)
    # print(p2)



