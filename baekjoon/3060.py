T = int(input())
for test in range(1, T+1):
    N = int(input())
    pig = list(map(int, input().split()))

    cnt = 1
    while True:
        d = [0]*6
        if sum(pig) > N:
            print(cnt)
            break
        for i in range(6):
            if i == 0:
                d[i] = pig[i]+pig[1]+pig[5]
                
            elif i == 5:
                d[i] = pig[i]+pig[4]+pig[0]

            else:
                d[i] = pig[i-1]+pig[i]+pig[i+1]
        cnt += 1
        if sum(d) > N:
            print(cnt)
            break

