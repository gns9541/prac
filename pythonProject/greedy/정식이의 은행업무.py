T = int(input())
for test_case in range(1, T + 1):
    s = list(map(int, input()))
    t = list(map(int, input()))

    lst = []
    for i in range(len(s)):
        for j in range(len(t)):
            lst.append([i,j])
    print(lst)

    for i in lst:

        if s[i[0]] == 1:
            s[i[0]] = 0
        elif s[i[0]] == 0:
            s[i[0]] = 1
        if t[i[1]] == 2:
            while True:
                t[i[1]] = 1
