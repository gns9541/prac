# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    for idx in range(N-1, 0, -1):
        for j in range(0, idx):
            if a[j] < a[j+1]:
                a[j], a[j + 1] = a[j+1], a[j]
    final = a[0] - a[N-1]
        # print(N)
        # print(a)
    print(f"#{test_case} {final}")


