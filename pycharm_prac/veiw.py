T = int(input())
for test_case in range(1, T + 1):
    buildings = list(map(int, input().split()))
    print(buildings)

    for i in range(len(buildings)-4): #14이면 (0,10)
        cnt = 0
        # m = buildings[i+2]
        # r1 = buildings[i+3]
        # r2 = buildings[i+4]
        # l1 = buildings[i+1]
        # l2 = buildings[i]
        lst = []
        for j in range(i, i+5):
            lst.append(buildings[j])

        m = lst[2]
        for idx in range(4, 0, -1):
            for jdx in range(0, idx):
                if lst[jdx] < lst[jdx+1]:
                    lst[jdx], lst[jdx + 1] = lst[jdx+1], lst[jdx]
        light = m-lst[0]
        # if m-lst[0] < 0:
        #     pass
        # if m-lst[0] > 0:
        #     print(m-lst[0])
        print(light)
        # print(m)
        # print(lst)



# 0 0 3 5 2 4 9 0 6 4 0 6 0 0