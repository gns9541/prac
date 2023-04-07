T = int(input())
for test in range(1, T+1):
    words = [list(map(str, input())) for _ in range(5)]
    N = 0
    for i in range(5):
        n = len(words[i])
        if n > N:
            N = n
    lst = []
    for j in range(N):
        for i in range(5):
            if len(words[i])<N:
                for k in range(N - len(words[i])):
                    words[i].append('')
            lst.append(words[i][j])
    final = []
    for i in lst:
        if i != '':
            final.append(i)
    ans = "".join(final)
    print(f"#{test} {ans}")

