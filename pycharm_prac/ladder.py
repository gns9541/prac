T = int(input())
for test_case in range(1, T + 1):
    L = [list(map(int, input().split())) for _ in range(100)]
    # print(*L, sep="\n")

    di = [0, 1, 0]  # 우 하 좌
    dj = [1, 0, -1]

    for k in range(3):
        ni = i +di[k]
        nj = j +dj[k]





    start = []
    for j in range(100):
        if L[0][j] == 1:
            start.append(j)
    i = 0
    for j in start:
        while 0 <= i < 100 or 0 <= j < 100:
            if L[i][j+1] == 1:
                j += 1
                if i == 98:
                    break
            if L[i][j-1] == 1:
                if i == 98:
                    break
                if j-1 < 0:
                    pass
                else:
                    j -= 1
            if L[i+1][j] == 1:
                if i == 98:
                    break
                else:
                    i += 1

            print(i, j)




    for i in range(100):
        if L[99][i] == 2:
            print("2", i)
