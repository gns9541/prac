# 관찰가능 방향 4개 이상인 지점에서 본인보다 작으면 cnt +=1

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    area = [[10]*(M+2)]+[[10]+list(map(int, input().split()))+[10] for _ in range(N)]+[[10]*(M+2)]
    # print(*area, sep="\n")

    di = [-1, 1, 0, 0, -1, 1, -1, 1] # 상 하 좌 우 대상우 대하우 대상좌 대하좌
    dj = [0, 0, -1, 1, 1, 1, -1, -1]

    final = []
    for i in range(1,N+1):
        for j in range(1,M+1):
            cnt = 0
            for k in range(8):
                if area[i][j] > area[i+di[k]][j+dj[k]]:
                    cnt += 1
            final.append(cnt)
    # print(final)
    count = 0
    for i in final:
        if i >=4:
            count += 1
    print(f"#{test_case} {count}")

