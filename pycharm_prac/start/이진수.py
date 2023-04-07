T = int(input())
for test in range(1, T+1):
    N = list(map(str,input()))
    print(N)
    n = ''.join(N)
    n = float(n)
    print(n)

    ans = 0
    k = [0]*14
    sum = 0
    i = 2
    # for i in range(2,len(N)):
    while True:
        sum += 2 ** (-(i - 1))
        k[i] = 1
        print(sum)
        if sum == n:
            ans = sum
            break
        # k[i] = 2**(-(i-1))

        elif sum > n:
            sum -= 2**(-(i-1))
            k[i] = 0
            sum += 2**(-i)
            k[i+1] = 1
            if sum == n:
                ans = sum
                break
        i += 1
        if i>12:
            ans = 'overflow'
            break
    print(k)
    #
    print(sum)
