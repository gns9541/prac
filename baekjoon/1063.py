# from collections import deque
# import sys
# input = sys.stdin.readline

N, K = map(int, input().split())
C = list(map(int, input().split()))

mx = -1000000
i = 0
sum = 0
while True:
    if i == N-K+1:
        break
    if i == 0:
        for k in range(K):
            sum += C[i+k]

    else:
        sum = sum - C[i-1] + C[i+K-1]
    
    if sum > mx:
        mx = sum
    i += 1
print(mx)







# while True:
#     if len(C) == K-1:
#         break
#     elif j == K:
#         if sum > mx:
#             mx = sum
#         C.popleft()
#         j = 0
#         sum = 0
#     else:
#         sum += C[0+j]
#         j+=1
# print(mx)

# mx = -100
# while True:
#     if len(C) == K-1:
#         break
#     sum = 0
#     for j in range(K):
#         sum += C[0+j]
#     if sum > mx:
#         mx = sum
#     C.popleft()
# print(mx)

# mx = -100
# for i in range(N-K+1):
#     sum = 0
#     for j in range(K):
#         sum += C[i+j]
#         if sum > mx:
#             mx = sum
# print(mx)

