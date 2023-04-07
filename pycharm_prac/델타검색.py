T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 0, -1, 1] # 좌 우 상 하
    dj = [-1, 1, 0, 0]

    sum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                # sum = 0
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum += abs(lst[ni][nj]-lst[i][j])
    print(f"#{test_case} {sum}")
