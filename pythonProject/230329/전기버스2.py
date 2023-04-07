from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    lst.remove(N)
    # print(lst)
    a = N-lst[0]
    lst.remove(lst[0])

    fin = []
    for k in range(len(lst)+1):
        for i in combinations(lst,k):
            fin.append(list(i))
    print(fin)
    fin2 = []
    for i in fin:
        if sum(i)>=a:
            fin2.append(i)
    # print(fin2)
    ans = 100000
    for i in fin2:
        if len(i)<=ans:
            ans = len(i)
    print(f"#{test_case} {ans}")




