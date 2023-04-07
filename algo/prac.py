# # from itertools import combinations
 
# # T = int(input())
# # for test_case in range(1, T + 1):
# #     N,B = map(int, input().split())
# #     S = list(map(int, input().split()))
 
# #     j = 1
# #     # for i in combinations(S,3):
# #     #     print(i)
# #     lst=[]
# #     while True:
# #         if j == N+1:
# #             break
# #         for i in combinations(S,j):
# #             if sum(list(i))>=B:
# #                 lst.append(sum(list(i)))
# #         j+=1
         
# #     ans = min(lst)-B
# #     print(f"#{test_case} {ans}")


# T = int(input())
# for test_case in range(1, T + 1):
#     N,B = map(int, input().split())
#     S = list(map(int, input().split()))
#     # v = [0]*N

#     mn = 10000*20
#     ans = 0
#     def dfs(i,add):
#         global mn,ans
        
#         if i==N:
#             if add>=B:
#                 mn = min(add,mn)
#                 ans = mn-B
#                 return
#         else:
#             dfs(i+1,add+S[i])
#             dfs(i+1,add)

#     dfs(0,0)
#     print(f"#{test_case} {ans}")

# # def dfs(i, sm):
# #     global ans
# #     if i==n:
# #         if sm >= b:
# #             if ans > sm:
# #                 ans = sm
# #     else:
# #         dfs(i+1, sm+lst[i])
# #         dfs(i+1, sm)
 
# # t = int(input())
# # for tc in range(1, t+1):
# #     n, b = map(int, input().split()) # 점원 수, 높이
# #     lst = list(map(int, input().split()))
# #     ans = sum(lst)
# #     dfs(0,0) # idx, sm
# #     print(f'#{tc} {ans}')



def check(lst,k):
    k = True
    for i in range(1,7//2+1):
        for j in range(7-i):
            if lst[j:i+j] == lst[i+j:2*i+j]:
                k = False
    return k    

if check('4212313',True):
    print('a') 
else:
    print('b')

lst = [1,2,3]
lst+[1]