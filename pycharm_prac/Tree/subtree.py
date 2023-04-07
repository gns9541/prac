def pre(i):
    if i:
        ans.append(i)
        pre(c1[i])
        pre((c2[i]))


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    c1= [0]*(E+2)
    c2 = [0] * (E + 2)

    for i in range(0, len(lst), 2):
        p,c = lst[i], lst[i+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c
    ans = []
    pre(N)
    print(f"#{test_case} {len(ans)}")