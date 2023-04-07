T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    final = 0
    for i in range(0, N-1, 1):
        cnt = 0
        for j in range(i+1, N):
            if nums[i] > nums[j]:
                cnt += 1

        if final < cnt:
            final = cnt

        # print(cnt)
    print(f"#{test_case} {final}")


