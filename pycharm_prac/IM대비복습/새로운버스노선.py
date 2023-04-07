T = int(input())
for test in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)] # [버스종류, A, B]
    st_lst = []
    for i in range(N):
        station = [0]*1001
        if lst[i][0] == 1:
            for j in range(lst[i][1], lst[i][2]+1):
                station[j] = 1
        elif lst[i][0] == 2:
            if lst[i][1] % 2 == 0:
                for j in range(lst[i][1], lst[i][2] + 1):
                    if j%2 == 0:
                        station[j] = 1
            else:
                for j in range(lst[i][1], lst[i][2] + 1):
                    if j%2 != 0:
                        station[j] = 1
        elif lst[i][0] == 3:
            if lst[i][1] % 2 == 0:
                for j in range(lst[i][1], lst[i][2] + 1):
                    if j%4 == 0:
                        station[j] = 1
            else:
                for j in range(lst[i][1], lst[i][2] + 1):
                    if j%3 == 0 and j%10 != 0:
                        station[j] = 1
        # print(station)
        st_lst.append(station)
    final = []
    for i in range(1001):
        cnt = 0
        for k in st_lst:
            if k[i] == 1:
                cnt += 1
        final.append(cnt)
    print(f"#{test} {max(final)}")



