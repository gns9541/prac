T = int(input())
for test in range(1, T+1):
    N = int(input())
    sq = [list(map(str, input())) for _ in range(N)]

    final = []
    for lst in sq:
        k = []
        for j in range(N):
            if lst[j] == '#':
                k.append(j)
        # print(k)
        v = []
        if len(k)>0:
            for i in range(k[0], k[-1]+1):
                v.append(i)
            if v == k:
                final.append(k)
    # print(final)
    ans = 'no'
    for lst in final:
        if len(lst) == len(final) and len(final) != 0:
            ans = 'yes'

    print(f"#{test} {ans}")
