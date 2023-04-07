from itertools import product

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    min = 1000000

    def f(j, add):
        global min
        if j == N:
            if add < min:
                min = add
        elif add > min:
            return
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                f(j + 1, add + V[j][i])
                check[i] = 0
        return min


    print(f"#{test_case} {f(0, 0)}")