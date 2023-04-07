# T = int(input())
for test_case in range(1, 11):
    N = int(input())
    words = [list(input()) for _ in range(8)]

    cnt = 0
    for lst in words:
        for i in range(8-N+1):
            if lst[i:i+N] == lst[i:i+N][::-1]:
                cnt +=1
    words = list(zip(*words))

    for lst in words:
        for i in range(8-N+1):
            if lst[i:i+N] == lst[i:i+N][::-1]:
                cnt +=1

    print(f"#{test_case} {cnt}")





'''
                def isSym(lst, i, M):
                    for j in range(M // 2):
                        if lst[i + j] != lst[i + M - 1 - j]:
                            return False
                    return True


                def solve(arr):
                    for _ in range(2):  # 두 번 반복: 행과 열
                        for lst in arr:  # 한 행씩 찾기
                            for i in range(N - M + 1):
                                # [1] 슬라이싱으로 비교
                                # if lst[i:i+M] == lst[i:i+M][::-1]:
                                # [2] 직접 비교(절반만)
                                if isSym(lst, i, M):
                                    return lst[i:i + M]
                        # 행에서 못찾은 경우, 전치행렬로 변환후 재실행
                        arr = list(zip(*arr))
                    return -1  # 이 코드가 실행될리는 없지만...


                T = int(input())
                for test_case in range(1, T + 1):
                    N, M = map(int, input().split())
                    arr = [input() for _ in range(N)]

                    ans = solve(arr)
                    print(f'#{test_case} {"".join(map(str, ans))}')
'''

