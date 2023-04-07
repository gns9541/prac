def collatz(num):
    sum = 0
    while True:    
        if num % 2 == 0:
            num = num / 2
            sum = sum + 1
            # print(num)
            # print(sum)
        elif num == 1:
            # print(num)
            # print(sum)
            break
        else:
            num = num * 3 + 1
            sum = sum + 1
            # print(num)
            # print(sum)    
        if sum > 500:
            print(-1)
            break
    if sum < 500:
        print(sum)
    else:
        pass
    return


collatz(6) #=> 8
collatz(16) #=> 4
collatz(27) #=> 111
collatz(626331) #=> -1
