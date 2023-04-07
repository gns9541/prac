N = int(input())
switch = [2]+list(map(int, input().split()))
p = int(input())
st = [list(map(int, input().split())) for _ in range(p)] #성별, 받은 수
# print(switch)

for i in range(p):
    if st[i][0] == 1:
        for j in range(1,N+1):
            if j % st[i][1] == 0:
                if switch[j] == 0:
                    switch[j] = 1
                else:
                    switch[j] = 0
    else:
        k = 1
        l = st[i][1]
        while True:
            if 1<= l-k and l+k <=N:
                if switch[l-k] == switch[l+k]:
                    if switch[l-k] == 0:
                        switch[l-k] = 1
                        switch[l+k] = 1
                    else:
                        switch[l-k] = 0
                        switch[l+k] = 0
                else:
                    if switch[l] == 0:
                        switch[l] = 1
                    else:
                        switch[l] = 0
                    break
            else:
                if switch[l] == 0:
                    switch[l] = 1
                else:
                    switch[l] = 0
                break    
            k += 1
    # print(switch)
switch.pop(0) 
for i in range(1, len(switch) + 1):
    print(switch[i - 1], end=' ')
    if i % 20 == 0:
        print()
     


