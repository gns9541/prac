def inorder(i):
    if i>0:
        inorder(c1[i])
        final.append(lst[i-1][1])
        inorder((c2[i]))

# T = int(input())
for test_case in range(1, 11):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]

    # print(*lst)
    c1 = [0]*(N+1)
    c2 = [0]*(N+1)
    for i in lst:
        p = int(i[0])
        if len(i)>3:
            if c1[p] == 0:
                c1[p] = int(i[2])
            if c1[p] != 0:
                c2[p] = int(i[3])
        elif len(i)==3:
            if c1[p] == 0:
                c1[p] = int(i[2])
    # print(c1)
    # print(c2)
    final = []
    inorder(1)
    ans = "".join(final)
    print(f"#{test_case} {ans}")



