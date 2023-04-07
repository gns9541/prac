from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))









    w = sorted(w)
    t = sorted(t)
    w.reverse()
    t.reverse()
    lst = []
    lst2 = []
    for i in range(len(w)):
        for j in range(len(t)):
            if w[i] <= t[j] and j not in lst2:
                lst.append(w[i])
                lst2.append(j)
                break
            else:
                pass
    ans = sum(lst)
    print(f"#{test_case} {ans}")












    # if N>M:
    #     lst = (list(combinations(w,M)))
    #     for i in lst:
    #         for j in t:
    #             if sum(i)>sum(t):
    #                 lst.remove(i)
    #     print(lst)
    #     mx = 0
    #     for i in lst:
    #         for j in i:
    #             for k in t:
    #                 if j>k:
    #                     lst.remove(i)
    #     print(lst)
    #     for i in lst:
    #         if sum(i)>mx:
    #             mx = sum(i)
    #     ans = mx
    # else:
    #     w=sorted(w)
    #     t=sorted(t)
    #     w.reverse()
    #     t.reverse()
    #     lst = []
    #     lst2=[]
    #     for i in range(len(w)):
    #         for j in range(len(t)):
    #             if w[i]<=t[j] and j not in lst2:
    #                 lst.append(w[i])
    #                 lst2.append(j)
    #                 break
    #             else:
    #                 pass
    #     ans = sum(lst)


