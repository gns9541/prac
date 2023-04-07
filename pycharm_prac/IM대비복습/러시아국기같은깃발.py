T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(N)]
    lst1 = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            lst1[i][j] = lst[i][j]

    lstW = []
    lstB = []
    lstR = []
    for i in range(N):
        W = 0
        B = 0
        R = 0
        for j in range(M):
            if lst[i][j] == 'W':
                W += 1
            elif lst[i][j] == 'B':
                B += 1
            elif lst[i][j] == 'R':
                R += 1
        lstW.append(W)
        lstB.append(B)
        lstR.append(R)
    count = [lstW, lstB, lstR]
    # print(*count, sep = "\n")
    cnt = 0
    wcnt = 0
    bcnt = 0
    rcnt = 0
    for i in range(N):
        for j in range(M):
            if i == 0:
                if lst[i][j] != 'W':
                    lst[i][j] = 'W'
                    cnt += 1
            if i == N-1:
                if lst[i][j] != 'R':
                    lst[i][j] = 'R'
                    cnt += 1
            else:
                if wcnt < (N-2)*M:
                    if count[0][i] >= count[1][i] and count[0][i] >=count[2][i]:
                        if lst[i][j] != 'W':
                            lst[i][j] = 'W'
                            cnt += 1
                        wcnt += 1
                elif wcnt == (N-2)*M:
                    if lst[i][j] != 'B':
                        lst[i][j] = 'B'
                        cnt += 1
                    # bcnt += 1
                elif bcnt < (N-2)*M:
                    if count[1][i] >= count[0][i] and count[1][i] >=count[2][i]:
                        if lst[i][j] != 'B':
                            lst[i][j] = 'B'
                            cnt +=1
                        bcnt += 1
                elif rcnt < (N-2)*M:
                    if count[2][i] >= count[0][i] and count[2][i] >=count[1][i]:
                        if lst[i][j] != 'R':
                            lst[i][j] = 'R'
                            cnt +=1
                        rcnt += 1
    wcnt1 = M
    bcnt1 = 0
    rcnt1 = M
    cnt1 = 0
    for i in range(N-1, -1, -1):
        for j in range(M):
            if i == 0:
                if lst1[i][j] != 'W':
                    lst1[i][j] = 'W'
                    cnt1 += 1

            elif i == N-1:
                if lst1[i][j] != 'R':
                    lst1[i][j] = 'R'
                    cnt1 += 1


            else:
                if rcnt1 < (N-2)*M:
                    if count[2][i] >= count[0][i] or count[2][i] >=count[1][i]:
                        if lst1[i][j] != 'R':
                            lst1[i][j] = 'R'
                            cnt1 +=1
                        rcnt1 += 1
                elif rcnt1 == (N-2)*M:
                    if lst1[i][j] != 'B':
                        lst1[i][j] = 'B'
                        cnt1 += 1
                    # bcnt += 1
                elif bcnt1 < (N-2)*M:
                    if count[1][i] >= count[0][i] or count[1][i] >=count[2][i]:
                        if lst1[i][j] != 'B':
                            lst1[i][j] = 'B'
                            cnt1 +=1
                        bcnt1 += 1
                elif wcnt1 < (N-2)*M:
                    if count[0][i] >= count[1][i] or count[0][i] >= count[2][i]:
                        if lst1[i][j] != 'W':
                            lst1[i][j] = 'W'
                            cnt1 += 1
                        wcnt1 += 1

    # print(*lst1, sep='\n')
    print(cnt, cnt1)
    if cnt >= cnt1:
        print(f"#{test} {cnt1}")
    else:
        print(f"#{test} {cnt}")









