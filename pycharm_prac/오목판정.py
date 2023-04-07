T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    st = [input() for _ in range(N)]
    ans = "NO"

    #가로
    cnt = 0
    for lst in st:
        for i in range(N):
            for j in range(i, N-5+1):
                if lst[j] == 'o':
                    cnt += 1
            if cnt >= 5:
                ans = "YES"
    #세로
    st_rev = list(zip(*st))
    for lst in st_rev:
        for i in range(N):
            for j in range(i, N - 5 + 1):
                if lst[j] == 'o':
                    cnt += 1
            if cnt >= 5:
                ans = "YES"
    #대각
    cnt_dagak1 = 0
    cnt_dagak2 = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                if st[i][j] == 'o':
                    cnt_dagak1 += 1
    for i in range(N):
        for j in range(N):
            if i+j == N-1:
                if st[i][j] == 'o':
                    cnt_dagak2 += 1

    if cnt_dagak1 >= 5 or cnt_dagak2 >= 5:
        cnt +=1
    if cnt == 0:
        ans = "NO"
    else:
        ans = "YES"
    print(f"#{test_case} {ans}")