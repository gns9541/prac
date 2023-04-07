T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))
    cnt = [0]*10
    for i in card:
        cnt[i] += 1

    cnt_max = []
    for x in range(len(cnt)):
        cnt_max.append(cnt[x])

    for idx in range(9, 0, -1):
        for j in range(0, idx):
            if cnt_max[j] > cnt_max[j+1]:
                cnt_max[j], cnt_max[j + 1] = cnt_max[j+1], cnt_max[j]

    max_num_num = cnt_max[9]
    max_num = cnt.index(max_num_num)

    for y in range(8, 0, -1):
        if cnt_max[9] == cnt_max[y]:
            max_num = y
            # print(max_num)

            break
        else:
            pass

    # print(cnt)
    # print(cnt_max)

    print(f"#{test_case} {max_num} {max_num_num}")







