T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    queue = [0] * N
    for _ in range(M):
        queue.append(num[0])
        num.pop(0)
        num.insert(N-1,queue[-1])
        queue.pop()

    print(f"#{test_case} {num[0]}")
