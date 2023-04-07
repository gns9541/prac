A = [1,2,3,4,5,6,7,8,9,10,11,12]
T = int(input())
for test_case in range(1, T + 1):
    # arr = [[]]
    # fin = []
    #
    N,K = map(int, input().split())
    #
    # for i in A:
    #     l = len(arr)
    #     for j in range(l):
    #         arr.append(arr[j]+[i])
    # for lst in arr:
    #     if len(lst) == N:
    #         if sum(lst) == K:
    #             fin.append(lst)
    #
    # ans = len(fin)
    # print(f"#{test_case} {ans}")

#############################################################


    # mainloop에서는 dfs의 가장 위 노드를 호출
    # i, cnt, 합

    def dfs(i,cnt,sm):
        global ans
        # 종료조건 & 정답처리
        if i == len(A):
            if cnt == N and sm == K:
                ans += 1
            print(ans)
        dfs(i+1, cnt+1, sm+A[i]) # 사용하는경우
        dfs(i+1, cnt, sm) # 사용하지 않는 경우

    ans = 0
    dfs(0,0,0)