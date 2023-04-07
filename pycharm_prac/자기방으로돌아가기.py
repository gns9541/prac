T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt = [0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        if s>e:
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2+1):
            cnt[i]+= 1
    ans = max(cnt)
    print(f"#{test_case} {ans}")
    # 방번호-1//2 : 복도번호
