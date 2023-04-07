T = int(input())
for test in range(1, T+1):
    N,M = map(int, input().split())
    code = [list(map(int, input())) for _ in range(N)]
    code_lst = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1], [0,0,1,0,0,1,1], [0,1,1,1,1,0,1], [0,1,0,0,0,1,1], [0,1,1,0,0,0,1],[0,1,0,1,1,1,1], [0,1,1,1,0,1,1], [0,1,1,0,1,1,1], [0,0,0,1,0,1,1]]

    c = []
    for i in code:
        if sum(i) != 0:
            c=i
            break

    i = 0
    while True:
        lst = []
        final_code = []
        if c[0:7] in code_lst:
            for i in range(0, len(c), 7):
                lst.append(c[i:i + 7])
            print(lst)
            cnt = 0
            for i in lst:
                if i in code_lst:
                    final_code.append(code_lst.index(i))
                    cnt +=1
            if cnt == 8:
                break
            else:
                c.pop(i)
        else:
            c.pop(i)

    sum1 = 0
    sum2 = 0
    for i in range(len(final_code)-1):
        if i%2 == 0:
            sum1 += final_code[i]
        else:
            sum2 += final_code[i]
    if (sum1*3+sum2+final_code[-1])%10 == 0:
        print(f"#{test} {sum(final_code)}")
    else:
        print(f"#{test}", 0)

