T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]

    ans = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for idx in range(M):
                for jdx in range(M):
                    sum += nums[i+jdx][j+idx]
            ans.append(sum)

    print(f"#{test_case} {max(ans)}")