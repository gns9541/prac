N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
v = [0]*N
ans = 1000000000
def cal(arr):
    synergy = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            synergy += S[arr[i]][arr[j]]+S[arr[j]][arr[i]]
            return synergy
def dfs(n,k):
    global ans
    if n == N//2:
        A=[]
        B=[]
        for i in range(N):
            if v[i] == 0:
                A.append(i)
            else:
                B.append(i)
            # print(A)
            # print(B)
        if ans > abs(cal(A)-cal(B)):
            ans = abs(cal(A)-cal(B))
        return
    for i in range(k,N):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1,i+1)
            v[i] = 0
dfs(0,0)
print(ans)