T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()
    A_new = A.replace(B, "0")
    ans = len(A_new)

    print(f"#{test_case} {ans}")



    # cnt = 0
    # for i in range(len(A)-len(B)+1):
    #     if A[i:i+len(B)] == B:
    #         # A[i:i+len(B)]
    #         cnt += 1
    #
    #         print(A[i:i + len(B)])
    # ans = len(A) - len(B)*cnt + 1*cnt

    # while True:
