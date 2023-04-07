from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    A = list(map(int, input().split()))

    j = 1
    lst = []
    while True:
        if j == N+1:
            break
        for i in combinations(A, j):
            lst.append(list(i))
        j += 1
    # print(lst)

    ans = 0
    for i in lst:
        if sum(i) == K:
            ans += 1

    print(f"#{test_case} {ans}")