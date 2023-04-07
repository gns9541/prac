T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    cnt_d = 0
    cnt_e = 0

    while 2<= N <=10**8:
        if N % 2 == 0:
            N = N/2
            cnt_a += 1
            continue
        elif N % 3 == 0:
            N = N/3
            cnt_b += 1
            continue
        elif N % 5 == 0:
            N = N/5
            cnt_c += 1
            continue
        elif N % 7 == 0:
            N = N/7
            cnt_d += 1
            continue
        elif N % 11 == 0:
            N = N/11
            cnt_e += 1
            continue
        if N < 2:
            break

    print(f"#{test_case} {cnt_a} {cnt_b} {cnt_c} {cnt_d} {cnt_e}")

