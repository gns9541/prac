T = int(input())
for test_case in range(1, T + 1):
    nums = int(input())
    c = [0]*12
    for i in range(6):
        c[nums % 10] += 1
        nums //= 10
    # print(c)
    idx = 0
    tri = runs = 0
    while idx < 10:
        if c[idx] >= 3: # triplet 조사
            c[idx] -= 3
            tri += 1
            continue
        if c[idx] >=1 and c[idx+1] >= 1 and c[idx+2] >=1 : # run 조사
            c[idx] -= 1
            c[idx+1] -= 1
            c[idx+2] -= 1
            runs += 1
            continue
        idx += 1
    if tri + runs == 2:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
