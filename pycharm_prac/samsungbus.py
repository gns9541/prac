T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    cnts = [0]*5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E+1):
            cnt[i]+=1

    p = int(input())
    alst = []
    for _ in range(p):
        p = int(input())
        alst.append(cnts[p])

    print(f'#{test_case}', *alst)