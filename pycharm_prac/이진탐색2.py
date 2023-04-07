T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    lst_P = []
    for i in range(0, P+1):
        lst_P.append(i)

    l = 1
    r = P
    cnt_A = 0
    while l <= r:
        mid = int((l+r)/2)
        if lst_P[mid] == A:
            cnt_A += 1
            break
        elif lst_P[mid] < A:
            l = mid
            cnt_A += 1
        elif lst_P[mid] > A:
            r = mid
            cnt_A += 1
        if A not in lst_P:
            break
        # print(lst_P[mid])

    l = 1
    r = P
    cnt_B = 0
    while l <= r:
        mid = int((l+r)/2)
        if lst_P[mid] == B:
            cnt_B += 1
            break
        elif lst_P[mid] < B:
            l = mid
            cnt_B += 1
        elif lst_P[mid] > B:
            r = mid
            cnt_B += 1
        if B not in lst_P:
            break
        # print(lst_P[mid])

    if cnt_A == cnt_B:
        print(f"#{test_case}", 0)
    elif cnt_A > cnt_B:
        print(f"#{test_case} B")
    elif cnt_A < cnt_B:
        print(f"#{test_case} A")
    # print(cnt_A, cnt_B)