T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    E = [[0]*(N+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]
    print(*E, sep="\n")

    ans = 100000000
    def perm(i, k):
        global ans
        if i == k:
            fin = []
            for j in range(len(p)-1):
                fin.append(E[p[j]][p[j+1]])
            fin.append(E[p[-1]][p[0]])
            print(sum(fin))
            if sum(fin) <= ans:
                ans = sum(fin)

        else:
            for j in range(i, k):
                p[i], p[j] = p[j], p[i]
                perm(i + 1, k)
                p[i], p[j] = p[j], p[i]

    p = []
    for i in range(1,N+1):
        p.append(i)
    print(p)
    perm(1, len(p))

    print(f"#{test_case} {ans}")
