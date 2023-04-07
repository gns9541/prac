T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    C = list(map(int, input()))

    # print(C)

    cnt = 1
    lst = []
    for j in range(N-1):
        if C[j] == 1 and C[j+1] == 1:  #
            # j = j+1
            cnt += 1
            lst.append(cnt) # 쌓인 카운트를 리스트로
        elif (C[j] == 0 and C[j+1] == 1) or (C[j] == 1 and C[j+1] == 0) or (C[j] == 0 and C[j+1] == 0): #
            cnt = 1
            lst.append(cnt)

    # print(lst)
    for i in range(len(lst)-1, 0, -1): # 리스트에 쌓인 카운트 중 가장 큰 수 꺼내기
        for j in range(0,i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j + 1] = lst[j+1], lst[j]
    print(f"#{test_case} {lst[-1]}")