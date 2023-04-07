T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(N, M)
    # print(A, B)
    # ans = []

    if N >= M:
        A, B = B, A
        # ans = []
        # lst = [0]*N
        # for i in range(len(B)):
        #     lst[i] = B[i]
        # # ans = []
        #
        # for j in range(0, len(B)):
        #     x = 0
        #     for i in range(len(lst)):
        #         x += lst[i] * A[i]
        #
        #     for idx in range(len(lst)-1, 0, -1):
        #         lst[idx] = lst[idx-1]
        #     lst[j] = 0
        #     ans.append(x)
        #
        # print(f"#{test_case} {(ans)}")

    # elif M > N:
    ans = []
    lst = [0]*M

    for i in range(len(A)):
        lst[i] = A[i]
        # ans = []

    for j in range(0, len(A)):
        x = 0
        for i in range(len(lst)):
            x += lst[i] * B[i]

        for idx in range(len(lst)-1, 0, -1):
            lst[idx] = lst[idx-1]
        lst[j] = 0
        ans.append(x)

    print(f"#{test_case} {max(ans)}")

