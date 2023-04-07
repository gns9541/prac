
for test_case in range(1, 11):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    lst_line = []

    for i in range(100):
        garo = 0
        sero = 0
        for j in range(100):
            garo += lst[i][j]
            sero += lst[j][i]
        lst_line.append(garo)
        lst_line.append(sero)

    dagak1 = 0
    dagak2 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                dagak1+=lst[i][j]
            if i+j == 99:
                dagak2+=lst[i][j]
    lst_line.append(dagak1)
    lst_line.append(dagak2)

    mx = 0
    for i in lst_line:
        if i > mx:
            mx = i
    print(f"#{test_case} {mx}")


######################################################################################
# 3개씩 계속 새로 더할 필요가 없다
# 앞에 거 하나를 빼주고 뒤에 하나 추가해주면 됨


