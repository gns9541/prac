N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

room = [[0]*3 for _ in range(6)]
for i in range(1,7):
    room[i-1][0] = i
# print(*room, sep="\n")
for j in room:
    for i in lst:
        if j[0] == i[1]:
            if i[0] == 0:
                j[1]+=1
            else:
                j[2]+=1
# print(*room, sep="\n") # 학년 여자수 남자수

ans = 0
for i in room:
    if i[1]>K:
        if i[1]%K != 0:
            ans += i[1]//K+1
        else:
            ans += i[1]//K
    elif K>=i[1]>0:
        ans += 1
     
    if i[2]>K:
        if i[2]%K != 0:
            ans += i[2]//K+1
        else:
            ans += i[2]//K
    elif K>=i[2]>0:
        ans += 1

print(ans)

