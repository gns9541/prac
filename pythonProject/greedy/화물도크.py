T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # t = [list(map(int, input().split())) for _ in range(N)]
    #
    # t.sort(key=lambda x: x[1])
    # print(t)

    time = []

    for _ in range(N):
        s, e = map(int, input().split())
        time.append([s, e])

    time = sorted(time, key=lambda a: a[0])
    time = sorted(time, key=lambda a: a[1])
    # print(time)
    end = 0  # 회의의 마지막 시간을 저장할 변수
    ans = 0  # 회의 개수를 저장할 변수

    for i, j in time:
        if i >= end:  # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
            ans += 1
            end = j

    print(f"#{test_case} {ans}")

    # def f(i):
    #     k = 1
    #     cnt = 0
    #     lst=[]
    #     while True:
    #         if i+k == len(t):
    #             f(i + 1)
    #             return
    #         elif t[i][1]>t[i+k][0]:
    #             # print(t[i+k])
    #             t.remove(t[i+k])
    #             k-=1
    #             cnt += 1
    #         else:
    #             pass
    #         k+=1
    #         print(t)
    #     # f(i+1)
    # print(f(0))
