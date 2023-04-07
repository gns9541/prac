T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    E = [[0]*N]+[[0]+list(map(int,input().split())) for _ in range(N)]

    ans = 100000000
    def perm(i, k):  # i:값 결정할 자리, k: 결정할 개수
        global ans
        if i == k:

            fin = []
            for j in range(len(p)-1):
                fin.append(E[p[j]][p[j+1]])
            fin.append(E[p[-1]][p[0]])
            # print(sum(fin))
            if sum(fin) <= ans:
                ans = sum(fin)

        else:
            for j in range(i, k):  # 자신부터 오른쪽 원소들과 교환
                p[i], p[j] = p[j], p[i]
                perm(i + 1, k)
                p[i], p[j] = p[j], p[i]

    p = []
    for i in range(1,N+1):
        p.append(i)
    perm(1, len(p))

    print(f"#{test_case} {ans}")
