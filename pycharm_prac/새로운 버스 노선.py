T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    B = [list(map(int, input().split())) for _ in range(N)]
    # print(B)
    # B[][0] = 일반(1), 급행(2), 광역(3)인지
    # B[][1] = A 정류장 번호
    # B[][2] = B 정류장 번호
    cnt = [0]*1500
    # print(cnt)
    for i in range(N):
        if B[i][0] == 1:
            for j in range(B[i][1]+1, B[i][2]): # 3 4
                cnt[j] += 1
            print(cnt)
        elif B[i][0] == 2:
            for j in range(B[i][1]+1, B[i][2]): # 4 5 6 7 8 9
                if B[i][1]%2 == 0:
                    if j%2 == 0:
                        cnt[j] += 1
                elif B[i][1]%2 != 0:
                    if j%2 != 0:
                        cnt[j] += 1
            print(cnt)
        elif B[i][0] == 3:
            for j in range(B[i][1]+1, B[i][2]): # 3 4 5 6 7 8
                if B[i][1] % 2 == 0:
                    if j%4 == 0:
                        cnt[j] += 1
                elif B[i][1] % 2 != 0:
                    if j%3 == 0 and j%10 != 0:
                        cnt[j] += 1
            print(cnt)
        cnt[B[i][1]] += 1 # 2 3 2
        cnt[B[i][2]] += 1 # 5 10 9
    print(f"#{test_case} {max(cnt)}")






