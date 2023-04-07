T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    words = [input().split() for _ in range(N)]

    lst = sum(words, [])
    new1 = []
    for i in range(N):
        for j in range(N-M+1):
            new1_lst = lst[i][j:j+M]
            new1.append(new1_lst)
    print(new1)
    # print(list(new1))
    word_lst = []
    for i in new1:
        word = list(i)
        word_lst.append(word)
    # print(word_lst)
    for i in word_lst:
        i.reverse()
        new_i = "".join(i)

        for j in new1:
            if new_i == j:
                print(f"#{test_case} {j}")

    new2 = []
    final2 = []
    final_rev = []
    for j in range(N):
        for i in range(N-M+1):
            for k in range(M):
                new2_lst = lst[i+k][j]
                new2.append(new2_lst)

    for i in range(0, len(new2), M):
        final2.append(new2[i:i+M])
        final_rev.append(new2[i:i+M])
    for i in final_rev:
        i.reverse()
    for i in final_rev:
        if i in final2:
            x = "".join(i)
            print(f"#{test_case} {x}")

##################################################################################
ip = int(input())

for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(list(input()) for _ in range(n))
    dummy = 0
    ans = ''
    for i in range(n):
        for k in range(n - m + 1):
            for j in range(m // 2):
                if lst[i][k + j] == lst[i][k + m - j - 1]:
                    dummy = 1
                else:
                    dummy = 0
                    break
            if dummy == 1:
                for j in range(m):
                    ans = ans + lst[i][j+k]
                break
        if dummy == 1:
            break

        for k in range(n - m + 1):
            for j in range(m // 2):
                if lst[k + j][i] == lst[k + m - j - 1][i]:
                    dummy = 1
                else:
                    dummy = 0
                    break
            if dummy == 1:
                for j in range(m):
                    ans = ans + lst[j + k][i]
                break
        if dummy == 1:
            break

print(f'#{case} {ans}')
