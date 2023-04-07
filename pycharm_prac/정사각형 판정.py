T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    arr_new = sum(arr,[])
    while True:
        if '.' in arr_new:
            arr_new.remove('.')
        else:
            break

    ans = []
    cnt = 0
    for idx in range(1, N**2+1):
        if len(arr_new) == idx*idx:
            print(idx)

        for i in range(N-idx+1):
            for j in range(N-idx+1):
                if arr[i][j] == "#":
                    for k in range(N-idx+1):
                        if arr[i][j+k] == "#":
                            cnt += 1
                        else:
                            pass
    print(cnt)
    # if "no" in ans:
    #     print(f"#{test_case}", "no")
    # else:
    #     print(f"#{test_case}", "yes")
    # print(*arr, sep="\n")
    # print(arr_new)
