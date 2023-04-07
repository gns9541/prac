from itertools import permutations
T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    lst1=[]
    lst2=[]

    def f(k):
        for i in permutations(k, 3):
            i=list(i)
            # print(i)
            if (i[0]+1 == i[1] and i[0]+2 == i[2]) or (i[0] == i[1] == i[2]):
                return True

    ans = 0
    for i in range(len(num)):
        if i%2==0:
            lst1.append(num[i])
            if f(lst1) == True:
                ans = 1
                break
        else:
            lst2.append(num[i])
            if f(lst2) == True:
                ans = 2
                break
        # print(lst1)
        # print(lst2)
        # print()
    print(f"#{test_case} {ans}")




