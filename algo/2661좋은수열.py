def check(lst):
    for i in range(1, len(lst)//2+1):
        if lst[-i:] == lst[-(i*2):-i]:
                return False
    return True

def dfs(n):
    global ans
    if not check(n):
        return
    if len(n) == N:
        ans = min(ans, int(n))
        print(ans)
        exit(0)
        
    for j in range(3):
        if num[j] != n[-1]:
            dfs(n+num[j])
    

N = int(input())
num = ['1','2','3']
ans = 10**(N)

dfs(num[0])    



# def check(lst,k):
#     k = True
#     for i in range(1,N//2+1):
#         for j in range(N-i):
#             if lst[j:i+j] == lst[i+j:2*i+j]:
#                 k = False
#                 break
#     return k    

# def dfs(i):
#     global ans
#     i = "".join(i)
#     if ans>int(i):
#         return

#     if len(i) == N:
#         i = "".join(i)
#         if ans<int(i):
#             return
#         if check(i,True):
#             ans = min(ans, int(i))
#             return
#     else:
#         for j in range(3):
#             if num[j] != i:
#                 dfs(i+num[j])



# N = int(input())
# num = ['1','2','3']
# ans = 10**(N+1)
# for i in range(3):
#     dfs(num[i])
    
# print(ans)

        


    