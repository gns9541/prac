from itertools import product

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    check = [0]*N
    min = 1000000

    def f(n,add):
        global min
        if n == N:
            if add < min:
                min = add
        elif add>min:  # 가지치기는 항상 제일 위에 해준다, 가장 나중에 고민
            return
        for j in range(N):
            if check[j] == 0:
                check[j] = 1
                f(n+1, add+arr[n][j])
                check[j] = 0
        return min
    print(f"#{test_case} {f(0,0)}")







    # i = 0
    # k = 0
    # lst2 = []
    # lst3 = []
    # while True:
    #     if i == N*N:
    #         lst3.append(lst2)
    #         break
    #     elif lst1[i][0] != k:
    #         k+=1
    #         lst3.append(lst2)
    #         lst2 = []
    #     elif lst1[i][0] == k:
    #         lst2.append(lst1[i])
    #         i+=1
    #     # print(lst2)
    # print(lst3)
    #
    # fin = []
    # for i in product(*lst3, *lst3):
    #     i = list(i)
    #     fin.append(i)
    # print(fin)