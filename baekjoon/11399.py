N = int(input())
P = list(map(int, input().split()))

P.sort()
# print(P)
ans = 0
for i in range(N):
    for j in range(0, i+1):
        ans+=P[j]
print(ans)

