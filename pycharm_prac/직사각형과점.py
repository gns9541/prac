T = int(input())
for test_case in range(1, T + 1):
    square = list(map(int, input().split())) # 꼭짓점
    N = int(input()) # 점 개수
    dot = [list(map(int, input().split())) for _ in range(N)]
    X=[]
    Y=[]
    X_line = []
    Y_line = []
    # print(square)
    # print(*dot, sep="\n")

    for i in range(square[0]+1,square[2]):  # 변이 아니라 완전히 안에
        X.append(i)
    for i in range(square[1]+1, square[3]):
        Y.append(i)

    # print(X, Y)
    In = []
    line = []
    out = []

    for i in dot:
        if i[0] in X and i[1] in Y:
            In.append(i)
        elif (i[0] == square[0] and square[1]<= i[1] <= square[3]) or (i[0] == square[2] and square[1]<= i[1] <= square[3]):
            line.append(i)
        elif (i[1] == square[1] and square[0]<=i[0]<= square[2]) or (i[1] == square[3] and square[0]<=i[0]<= square[2]):
            line.append(i)
        else:
            out.append(i)
    print(f"#{test_case} {len(In)} {len(line)} {len(out)}")

