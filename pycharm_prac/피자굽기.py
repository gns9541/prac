T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    queue = []
    q2 = []
    for _ in range(N):
        queue.append(num[0])
        num.pop(0)
        q2.append(queue[-1])
        # queue.pop()
    print(queue)
    print(num)