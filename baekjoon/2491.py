N = int(input())
num = list(map(int, input().split()))
# print(N)
# print(num)

cnt_up = 1
cnt_down = 1
cnt = [] 
i = 0
if len(num) == 1:
    print(1)
else:
    while True:
        if len(num) == 1:
            print(1)
            break

        if num[i] < num[i+1]:
            cnt.append(cnt_down)
            cnt_down = 1
            cnt_up +=1
            
        elif num[i] > num[i+1]:
            cnt.append(cnt_up)
            cnt_up = 1
            cnt_down +=1
        
        elif num[i] == num[i+1]:
            cnt_up += 1
            cnt_down += 1
        
        i += 1
        if i == N-1:
            cnt.append(cnt_down)
            cnt.append(cnt_up)
            break
    print(max(cnt))


