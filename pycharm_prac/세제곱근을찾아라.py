T = int(input())
ans = 0
for test_case in range(1, T+1):
    N = int(input())
    if round(N**(1/3))**3 == N:
        ans = round(N**(1/3))
    else:
        ans = -1
    print(f"#{test_case} {ans}")