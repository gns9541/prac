def preorder(i, ans):
    if i>0:
        ans.append(i)
        preorder(c1[i], ans)
        preorder((c2[i]), ans)


T = int(input())
for test_case in range(1, T + 1):
    V = int(input())
    lst = list(map(int, input().split()))
    c1 = [0] * (V + 1)
    c2 = [0] * (V + 1)
    p = []
    c = []
    for i in range(len(lst)):
        if i%2 == 0:
            p.append(lst[i])
        else:
            c.append(lst[i])
    for i in p:
        if c1[i] == 0:
            c1[i] = c[0]
            c.pop(0)
        else:
            c2[i] = c[0]
            c.pop(0)

    ans = []
    preorder(1, ans)
    print(f"#{test_case}", *ans)


