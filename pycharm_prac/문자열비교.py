T = int(input())
for test_case in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    N = len(str1)
    M = len(str2)

    new_lst = []
    final = []

    for i in range(M-N+1):
        new_lst = str2[i:i+N]
        final.append(new_lst)

    if str1 in final:
        print(f"#{test_case}", 1)
    else:
        print(f"#{test_case}", 0)



