T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    f = [list(map(int, input().split())) for _ in range(N)]
    # print(*f, sep="\n")

    di = [-1, 1, 0, 0] # 상 하 좌 우
    dj = [0, 0, -1, 1]

    lst = []
    for i in range(N):
        for j in range(M):
            P = f[i][j]
            cnt = P
            for p in range(1,P+1):
                for k in range(4):
                    ni, nj = i+p*di[k], j+p*dj[k]
                    if 0<=ni<N and 0<=nj<M:
                        cnt += f[ni][nj]
            lst.append(cnt)
    print(f"#{test} {max(lst)}")
