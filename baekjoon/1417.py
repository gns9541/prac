N = int(input())
p = [int(input()) for _ in range(N)]
print(p)


# for i in range(N):
i = 0
count = 0
while True:
    mx = 0
    for j in range(1,N):
        if p[j] > mx:
            mx = p[j]
    cnt = 0
    if cnt == N-1:
        
        break
    elif p[0] <= mx:
        p[0] += 1
        mx -= 1
        for k in range(N):
            if p[0] > p[k]:
                cnt += 1
        count += 1
    if cnt < N-1:
        cnt = 0
    if cnt == N-1:
        print(p)
        print(cnt)
        break
    i +=1
    if i == N-1:
        i = 0
  
    print(p)
    # print(cnt)
    print(count)

