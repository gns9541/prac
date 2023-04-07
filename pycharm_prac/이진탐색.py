T = int(input())
for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    nums = list(map(int, input().split()))

    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == D:
            print(f"#{test_case} {mid+1}")
            break
        elif nums[mid] < D:
            start = mid+1
        elif nums[mid] > D:
            end = mid-1
        if D not in nums:
            print(f"#{test_case}", 0)
            break
