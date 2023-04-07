T = int(input())
for test_case in range(1, T + 1):
    word = input()
    n = len(word)
    # print(n)
    lst = [["."]*(4*n+1) for _ in range(5)]
    # print(*lst, sep="\n")
    for i in range(5):
        if i == 2:
            k = 0
            while k <= 4*n+1:
                lst[2][k] = "#"
                if k == 4*n:
                    break
                else:
                    lst[2][k+1] = "."
                    lst[2][k+2] = word[k//4]
                k += 4
        elif i%2 != 0:
            k=0
            while k <= 4 * n + 1:
                lst[i][k] = "."
                lst[i][k+1] = "#"
                k+=2
                if k == 4*n:
                    break
        elif i % 2 == 0:
            k = 0
            while k <= 4 * n + 1:
                lst[i][k] = "."
                lst[i][k + 1] = "."
                lst[i][k + 2] = "#"
                lst[i][k + 3] = "."
                k += 4
                if k == 4 * n:
                    break

        print("".join(lst[i]))


