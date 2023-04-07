T = int(input())
for test in range(1, T+1):
    N,M,K = map(int, input().split()) # 사람, K개 만드는 시간
    a = list(map(int, input().split()))
    lst = [0]*(max(a)+1)
    for i in range(0, len(lst), M):
        if i != 0:
            lst[i] = K
    cnt = 0
    ans = 'Impossible'
    for i in a:
        for j in range(i,-1,-1):
            if lst[j] != 0:
                lst[j] -= 1
                cnt += 1
                break
    # print(lst)
    # print(cnt)
    if cnt == N:
        ans = 'Possible'
    print(f"#{test} {ans}")

