# def memory(N):
#     cnt = 0
#     for k in (0, 1):
#         for i in range(N):
#             for j in range(i, N):
#                 bit_new[j] = k
#                 cnt += 1
#                 if bit_new == bit:
#                     return cnt
#
# T = int(input())
# for test_case in range(1, T + 1):
#     n = input()
#     N = len(n)
#     bit = [0] * len(n)
#     bit_new = [0]*len(n)
#     for i in range(len(n)):
#         bit[i] = int(n[i])
#     print(bit)
#
#     ans = memory(N)
    # print(f"#{test_case} {ans}")
#########################################################################
# 앞값과 다른경우 ans +=1
T = int(input())
for test_case in range(1, T + 1):
    n = input()
    N = len(n)
    bit = [0]*N
    for i in range(N):
        bit[i] = int(n[i])
    bit.insert(0, 0)
    print(bit)
    ans = 0
    for i in range(len(bit)-1):
        if bit[i] != bit[i+1]:
            ans +=1
    print(f"#{test_case} {ans}")




