T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    words = [input().split() for _ in range(N)]

    lst = []

    for i in range(N):
        # for j in range(len(lst)):
        lst.append(words[i][0]*(int(words[i][1])))
    lst_new = "".join(lst)

    print(f"#{test_case}")
    for i in range(0,len(lst_new), 10):
        lst_fianl = lst_new[i:10+i]
        print(lst_fianl)
    # print(lst_new)