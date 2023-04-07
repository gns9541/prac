N, M, L = map(int, input().split())
lst = []
for i in range(N+1):
    lst.append(i)
v = [0]*(N+1)
v[1] = 1
i = 1
cnt = 0
while True:
    if M in v:
        break

    if v[i]%2 !=0:
        if i+L<=N:
            v[i+L]+=1
            i = i+L
        else:
            v[L-(N-i)]+=1
            i = L-(N-i)
    else:
        if i-L>=1:
            v[i-L]+=1
            i = i-L
        else:
            v[N-(L-i)]+=1
            i = N-(L-i)
    cnt += 1
print(cnt)

            
