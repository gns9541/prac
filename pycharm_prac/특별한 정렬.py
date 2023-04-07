T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    lst = [0]*10

    for i in range(len(lst)):
        if i == 0 or i%2 == 0:
            lst[i] = a.pop(a.index(max(a)))
        else :
            lst[i] = a.pop(a.index(min(a)))
    print(f"#{test_case}",*lst)
