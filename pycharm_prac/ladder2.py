T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100 * 100
    for sj in range(1, 101):
        # [1] 시작지점 찾기
        si = 0
        if arr[si][sj] != 1:
            continue
        cnt, dj = 0, 0
        ci, cj = si, sj
        while ci < 99:
            cnt += 1
            if dj == 0:
                if arr[ci][cj - 1] == 1:  # 좌측
                    dj = -1
                    cj -= 1
                elif arr[ci][cj + 1] == 1:  # 우측
                    dj = 1
                    cj += 1
                else:
                    ci += 1
            else:
                if arr[ci][cj + dj] == 1:
                    cj += dj
                else:  # 진행방향이 막힌경우 아래로
                    dj = 0
                    ci += 1
        if mn >= cnt:
            mn, ans = cnt, sj - 1

    print(f'#{test_case} {ans}')


'''
2차원 배열의 양끝에 0을 더한다 -> ans-1
1~100까지 -> 좌/우 : 1순위, 진행방향(1인경우)직진: 2순위 dj = [-1, 1, 0] 좌 우 아래
si = 0, sj = 1, cnt = 0, ci, cj, mn = 100*100
while ci < 99:  99되면 종료
    cnt +=1
    if dj == 0:  # 아래방향
        if arr[ci][cj-1] == 1 #좌
            dj = -1, cj -= 1
        elif arr[ci][cj+1] == 1 #우
            dj =1, cj += 1
        else:
            ci += 1
    else:  #좌/우 -> 직진(진행방향 1이면)
        if arr[ci][cj+dj] == 1:
            cj += dj
        else:    #아래
            dj = 0, ci += 1     
    
    if mn > cnt  #정답(sj좌표) 갱신   
        mn, ans = cnt, sj-1        
'''