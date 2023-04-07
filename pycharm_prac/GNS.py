T = int(input())
for test_case in range(1, T + 1):
    case, N = input().split()
    nums = input().split()
    print(f"#{test_case} ")
    # print(case, N)
    # print(nums)
    dic = {0:'ZRO', 1:'ONE', 2:'TWO',3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
    dic_rev = {}
    lst = []
    for k,v in dic.items():
        dic_rev[v] = k
    # print(dic_rev)
    for i in nums:
        for j in dic.values():
            if j == i:
                lst.append(dic_rev[i])
                lst.sort()
    # print(lst)
    for i in lst:
        for j in dic.keys():
            if i == j:
                print( dic[i],end=" ")
    print()
