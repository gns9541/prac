L = int(input())
N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
cake = [0]*(L+1)
expect = []
for i in range(len(num)):
    cnt = 0
    for k in range(num[i][0], num[i][1]+1):
        if cake[k] == 0:
            cake[k] = i+1
        cnt += 1
    expect.append(cnt)

real = []
for i in range(1,N+1):
    cnt = 0
    for j in range(len(cake)):
        if cake[j] == i:
            cnt += 1
    real.append(cnt)


print(expect.index(max(expect))+1)        
print(real.index(max(real))+1)