def cal(a, b, t):
    if t == 0:
        return a + b
    elif t == 1:
        return a - b
    elif t == 2:
        return a * b
    else:
        return int(a / b)


def dfs(idx, ans):
    if idx >= N:
        global mx, mn
        if ans > mx:
            mx = ans
        if ans < mn:
            mn = ans
        return
    for i in range(4):
        if t[i]:
            t[i] -= 1
            dfs(idx + 1, cal(ans, num[idx + 1], i))
            t[i] += 1


T = int(input())
for test in range(1, T + 1):
    N = int(input()) - 1
    t = list(map(int, input().split()))
    mx = -987654321
    mn = 987654321
    num = list(map(int, input().split()))
    dfs(0, num[0])
    # print('#{} {}'.format(t, max_n - min_n))
    print(f"#{test} {mx-mn}")



    # tlst = []
    # for i in range(len(t)):
    #     if i == 0:
    #         tlst.append(['+']*t[i])
    #     elif i == 1:
    #         tlst.append(['-']*t[i])
    #     elif i == 2:
    #         tlst.append(['*']*t[i])
    #     elif i == 3:
    #         tlst.append(['/']*t[i])
    #
    # lst = sum(tlst,[])
    # # print(lst)
    #
    # ans = []
    # for i in permutations(lst): ## 시간초과 무조건 뜸..DFS??
    #     i = list(i)
    #     # print(i)
    #     k = 0
    #     fin = [0]*(2*N-1)
    #
    #     while True:
    #         if k == 2*N-1:
    #             break
    #         if k%2 == 0:
    #             fin[k] = num[k//2]
    #             k+=1
    #         else:
    #             fin[k] = i[k//2]
    #             # fin.append(i[k//2])
    #             k+=1
    #     # ans.append(fin)
    # # print(f"#{test_case} {ans}")
    # #     fin = list(map(str, fin))
    # #     print(fin)
    #     for j in range(len(fin)):
    #         if fin[j] == '+':
    #             fin[j+1]=fin[j-1]+fin[j+1]
    #         elif fin[j] == '-':
    #             fin[j+1]=fin[j-1]-fin[j+1]
    #         elif fin[j] == '*':
    #             fin[j+1]=fin[j-1]*fin[j+1]
    #         elif fin[j] == '/':
    #             fin[j+1]=int(fin[j-1]/fin[j+1])
    #     ans.append(fin[-1])
    #     # print(ans)
