N, M = map(int, input().split())
card = list(map(int, input().split()))
lst = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            ans = card[i]+card[j]+card[k] 
            if ans <= M:
                lst.append(ans)
print(max(lst))