for test_case in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))
    cnt = 1
    while True:
        data.append(data[0]-cnt)
        data.pop(0)
        cnt += 1
        if cnt == 6:
            cnt = 1
        for i in range(len(data)):
            if data[i] < 0:
                data[i] = 0
        if data[-1] == 0:
            break
    print(f"#{test_case}", *data)
