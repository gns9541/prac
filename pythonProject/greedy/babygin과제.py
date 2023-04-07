from itertools import combinations
from copy import deepcopy

T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int,input()))
    num.sort()


    def dfs(n,r,s):
        global ans
        if r == 0:
            print(t)
            num2 = deepcopy(num)
            for i in t:
                num2.remove(i)
            # print(num2)
            if (t[0] + 1 == t[1] and t[0] + 2 == t[2]) and (num2[0] + 1 == num2[1] and num2[0] + 2 == num2[2]):
                ans = 1

            elif (t[0] == t[1] == t[2]) and (num2[0]+1 == num2[1] and num2[0]+2 == num2[2]):
                ans = 1

            elif (t[0]+1 == t[1] and t[0]+2 == t[2]) and (num2[0] == num2[1] == num2[2]):
                ans = 1

            elif (t[0] == t[1] == t[2]) and (num2[0] == num2[1] == num2[2]):
                ans = 1
        else:
            for i in range(s, n-r+1):
                t[r-1] = num[i]
                dfs(n,r-1,i+1)

    ans = 0
    t = [0] * 3
    dfs(6,3,0)
    # print(ans)
    print(f"#{test_case} {ans}")

    # ans = 0
    # for i in combinations(num, 3):
    #     i=list(i)
    #     num2 = deepcopy(num)
    #     for j in i:
    #         num2.remove(j)
    #     # print(i, num2)
    #     if (i[0]+1 == i[1] and i[0]+2 == i[2]) and (num2[0]+1 == num2[1] and num2[0]+2 == num2[2]):
    #         ans = 1
    #
    #     elif (i[0] == i[1] == i[2]) and (num2[0]+1 == num2[1] and num2[0]+2 == num2[2]):
    #         ans = 1
    #
    #     elif (i[0]+1 == i[1] and i[0]+2 == i[2]) and (num2[0] == num2[1] == num2[2]):
    #         ans = 1
    #
    #     elif (i[0] == i[1] == i[2]) and (num2[0] == num2[1] == num2[2]):
    #         ans = 1
    #
    # print(f"#{test_case} {ans}")


