N, L = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)] # D위치, R 빨간불 지속시간, G초록불

road = [0]*(L+1)
for i in lst:
    road[i[0]] = {'D':i[1]}
# print(road)

i = 1
time = 0
while True:
    if i == L+1:
        break
    if road[i] == 0:
        road[i] = 1
        i += 1
    else:
        if road[i]["D"]<=0:
            road[i] = 1
            i+=1
    for d in range(len(road)):
        if road[d] != 0 and road[d] != 1 :
            for k in lst:
                if d == k[0]:
                    if k[1]>= road[d]["D"] > -k[2]+1:
                        road[d]["D"] -= 1
                    elif road[d]["D"] == -k[2]+1:
                        road[d]["D"] = k[1]
                    
    time += 1
print(time-1)




    
    

