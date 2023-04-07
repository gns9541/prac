#중위순회
def inorder(i):
    if i>0:
        inorder(c1[i])
        final.append(i)
        inorder((c2[i]))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    c1 = [0]*(N+1)
    c2 = [0]*(N+1)
    lst = []
    for i in range(1, N+1):
        lst.append(i) # 1 2 3 4 5 6
    for i in lst:
        if c1[i] == 0:
            if 2*i <= N:
                c1[i] = 2*i
        if c1[i] != 0:
            if 2*i+1 <= N:
                c2[i] = 2*i+1
    final = [0]
    inorder(1)

    print(f"#{test_case} {final.index(1)} {final.index(N//2)}")

