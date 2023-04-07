N = int(input())
score = [list(input()) for _ in range(N)]
print(*score, sep="\n")

cnt_lst =[ ]
for i in score:
    j = 0
    cnt = 0
    lst = []
    while True:
        if i[j] == 'O':
            cnt += 1
            lst.append(cnt)
            j += 1
        elif i[j] == 'X':
            cnt = 0
            j += 1
        if j == len(i):
            break
    print(sum(lst))
