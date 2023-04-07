T = int(input())
for test_case in range(1, T + 1):
    num, change = map(int, input().split())
    num = str(num)
    num = [num[i:i+1] for i in range(0,len(num))]
    # print(num)
    ans = 0
    v = {}

    def dfs(num,cnt):
        global ans
        # if [num,cnt] in v:
        #     return
        if cnt == 0:
            if ans<int("".join(num)):
                ans = int("".join(num))
            return num
        for i in range(len(num)):
            for j in range(1, len(num) - i):
                num[i], num[i + j] = num[i + j], num[i]
                if v.get(("".join(num),cnt),True):
                    v[("".join(num),cnt)]=False
                    dfs(num, cnt - 1)
                num[i], num[i + j] = num[i + j], num[i]
        return

    dfs(num,change)
    print(f"#{test_case} {ans}")

