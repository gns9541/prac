T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]

    i = j = dr = 0 #초기값
    di = [0, 1, 0, -1]  # 우 하 좌 상
    dj = [1, 0, -1, 0]

    for cnt in (1, N*N+1):
        lst[i][j] = cnt #현재 좌표에 숫자
        ni, nj = i + di[dr], j + dj[dr]
        # 이동할 위치가 범위 내, 빈칸이 0인 경우 이동
        if (0 <= ni < N) and (0 <= nj < N) and (lst[ni][nj]) == 0:
            i,j = ni, nj
        else: #방향 꺾기
            dr = (dr+1)%4  # 0-1-2-3-1-2-...
            i,j = i + di[dr], j + dj[dr]

    for a in lst:
        print(*a)















    # num = 1
    # di = [0, 1, 0, -1]  # 우 하 좌 상
    # dj = [1, 0, -1, 0]
    # lst[0][0] = 1
    # cnt = 3
    # dir = "우"
    # i = j = 0

    #
    # while num < N:
    #     if dir == "우":
    #         for idx in range(cnt):
    #             num += 1
    #             i = i + di[0]
    #             j = j + dj[0]
    #             lst[i][j] = num
    #             if lst[i][j] != 0 or i==N or j==N:
    #                 dir = "하"
    #                 break
    #
    #     elif dir == "하":
    #         for udx in range(cnt):
    #             num += 1
    #             i = i + di[1]
    #             j = j + dj[1]
    #             lst[i][j] = num
    #             if lst[i][j] != 0 or i==N or j==N:
    #                 dir = "좌"
    #                 break
    #
    #     elif dir == "좌":
    #         for udx in range(cnt):
    #             num += 1
    #             i = i + di[2]
    #             j = j + dj[2]
    #             lst[i][j] = num
    #             if lst[i][j] != 0 or i==N or j==N:
    #                 dir = "상"
    #                 break
    #
    #     elif dir == "상":
    #         for udx in range(cnt):
    #             num += 1
    #             lst[i][j] = num
    #             i = i + di[2]
    #             j = j + dj[2]
    #             if lst[i][j] != 0 or i==N or j==N:
    #                 dir = "우"
    #                 break
    #
    # print(lst)
    #
    # for cnt in (1, N*N+1):
    #
    #
    #     if 0 <= ni < N,  0<= nj < N,  arr[ni][nj] == 0:
    #         i, j = i + di[dr], j + dj[dr]
    #     else: #꺾어야 하는 경우







    # for i in range(N):
    #     for j in range(N):
    #         for k in range(4):
    #             for l in range(1,N):
    #                 ni = i + di[k]
    #                 nj = j + dj[k]
    #                 lst[ni][nj] = num+1
    #                 num += 1
    #
    #                 if lst[ni][nj] != 0:
    #                     pass
    #                     N -= 1
    # print(*lst, sep='\n')







