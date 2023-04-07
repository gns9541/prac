T = int(input())
for test_case in range(1,T+1):
    K, N, M = map(int, input().split())
    bsc = [0] + list(map(int, input().split())) +[N]
    ans = s = 0

    for i in range(1, len(bsc)):
        # 정류장 사이가 K 이상: 도달 불가
        if bsc[i]-bsc[i-1]>K:
            ans = 0
            break
        #
        if bsc[i]-bsc[s] > K:
            ans += 1
            s = i-1
    print(f"#{test_case} {ans}")



    # bs = [0]*(N+1)
    # for i in range(0, N+1):
    #     for j in bsc:
    #         if j == i:
    #             bs[i] += 1
    # print(bs) # 충전소(1) 와 버정(0)
    #
    # cnt = K
    # for idx in range(0,len(bs)):
    #     if cnt == 0:
    #         print("fail")
    #         break
    #
    #     elif bs[0+idx] == 0: # or bs[0+idx] == 1:
    #         cnt -= 1
    #
    #     elif bs[0+idx] == 1:
    #         cnt = K











