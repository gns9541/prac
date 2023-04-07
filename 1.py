T = int(input())
for test_case in range(1, T+1):
    lst = [[0] * 10 for _ in range(10)]
    N = int(input()) # 2
    r, c = map(int, input().split()) # 3 3 망치 시작
    D = [list(map(int, input().split())) for _ in range(N)] # 1 2 2, # 3 4 3
    print(D)

    for i in range(N):
        point = 0
        A = D[i][0]
        B = D[i][1]
        K = D[i][2]

        cnt = 0
        while 0<=cnt:
            if B < c:
                c-=1
                cnt +=1

            elif B > c:
                c+=1
                cnt+=1

            elif B == r:
                if A < r:
                    r -= 1
                    cnt +=1
                elif A > r:
                    r += 1
                    cnt +=1
            if A == r and B == c:
                break
            if cnt == 2:
                break

        if cnt <= K:
            point += 1
        print(point)