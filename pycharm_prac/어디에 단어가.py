
'''
cnt 증가시키고 끝나면(0이 나오면 or 경계idx 나오는 경우) 길이비교
2차원배열 arr[]==1 -> cnt +=1, arr[]==0 -> cnt == 0
for lst in arr:
    cnt = 0
    for n in lst:
        if n == 1:  cnt +=1
        else:
            if cnt == k:  ans +=1
            cnt = 0
그 후 전치행렬로 다시 찾아보기
'''

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:        # 단어 넣을 수 있음
                cnt += 1
            else:             # 칸 없음
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    # arr 와 arr_t로 각각 개수 계산
    arr_t = list(zip(*arr))
    ans = count(arr) + count(arr_t)



    print(f"#{test_case} {ans}")




