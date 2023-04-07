T = int(input())
for test_case in range(1, T + 1):
    nums = [list(map(int, input().split())) for _ in range(9)]

    idx = 0
    lst = []
    cnt = []
    while idx < 9:
        for i in range(8):
            for j in range(1,8-i):
                if nums[idx][i] == nums[idx][i+j]:
                    cnt.append(0)
                    break
                else:
                    pass
        nums = list(zip(*nums))
        for i in range(8):
            for j in range(1, 8 - i):
                if nums[idx][i] == nums[idx][i + j]:
                    cnt.append(0)
                    break
                else:
                    pass
        idx += 1
    a = 0
    b = 0
    while a < 7 and b < 7:
        lst = []
        for i in range(a, a+3):
            for j in range(b, b+3):
                lst.append(nums[i][j])
        for i in range(8):
            for j in range(1,8-i):
                if lst[i] == lst[i+j]:
                    cnt.append(0)
        if a < 7:
            a += 3
        else:
            b += 3
    if 0 in cnt:
        print(f"#{test_case}", 0)
    else:
        print(f"#{test_case}",1)
