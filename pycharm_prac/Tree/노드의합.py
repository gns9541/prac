# # 후위순회
# def tree(i,j):
#     if i:
#         tree(c1[i][0],c1[i][1])
#         tree(c2[i][0],c2[i][1])
#         print(j)
#
#
#

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    num = [list(map(int, input().split())) for _ in range(M)]
    c1 = [[0,0]]*(N//2+1)
    c2 = [[0,0]] * (N//2+1)
    for i in range(1,N+1):
        if c1[i] == [0,0]:
            c1[i] = [i*2,0]
        if 2*i == N:
            break
        if c1[i] != 0:
            c2[i] = [i*2+1,0]
        if 2*i+1 == N:
            break
    for i in num:
        for j in range(len(c1)):
            if i[0] == c1[j][0]:
                c1[j] = [c1[j][0], i[1]]
        for j in range(len(c2)):
            if i[0] == c2[j][0]:
                c2[j] = [c2[j][0], i[1]]
    # 0         1      2      3         4         5
    #[[0, 0], [2, 0], [4, 0], [6, 501], [8, 42], [10, 335]]
    #[[0, 0], [3, 0], [5, 0], [7, 170], [9, 468], [0, 0]]

    for i in range(len(c1)-1,0,-1):  # c의 인덱스 5 4 3 2 1 0
        for j in range(len(c1)-1,0,-1): #
            if i == c1[j][0]: # 0 2 4 6 8 10
                c1[j][1] = c1[i][1] + c2[i][1]
        for j in range(len(c2)-1,0,-1): #
            if i in c2[j]:
                c2[j][1] = c1[i][1] + c2[i][1]

    if L%2 == 0:
        for i in c1:
            if i[0] ==L:
                print(f"#{test_case} {i[1]}")
    else:
        for i in c2:
            if i[0] ==L:
                print(f"#{test_case} {i[1]}")

    # lst = []
    # ans = num[0][1]
    # print(c1)
    # print(c2)

    # for i in lst:
    #     if i[0] == L:
    #         print(f"#{test_case} {i[1]}")
    # print(ans, lst)