T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [[0]*(N+1) for _ in range(N+1)]
    lst[1][1] = 1
    for i in range(2,N+1):
        for j in range(1, i+1):
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
    print(f'#{test_case}')

    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(f'{lst[i][j]}', end=' ')
        print()





