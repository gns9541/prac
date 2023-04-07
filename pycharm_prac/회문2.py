for test_case in range(1, 11):
    N = int(input())
    words = [list(input()) for _ in range(100)]

    n = 0
    cnt_lst = []
    while True:
        for lst in words:
            for i in range(100):
                for j in range(100-i):
                    if lst[i] == lst[i+j]:
                        jdx = 0
                        cnt = 0
                        while jdx <= j:
                            if lst[i+jdx]==lst[i+j-jdx]:
                                cnt +=1
                                jdx +=1
                            else:
                                break
                            if cnt == round(j/2)+1:
                                cnt_lst.append(j+1)
                                break
        if n == 2:
            break
        words = list(zip(*words))
        n+=1
    print(f"#{test_case} {max(cnt_lst)}")





