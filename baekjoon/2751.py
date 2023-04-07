N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if nums[i]>nums[i+j]:
            nums[i], nums[i+j] == nums[i+j], nums[i]
print(nums)