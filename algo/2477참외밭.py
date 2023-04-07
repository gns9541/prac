K = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]
# 1:오 2:왼 3:아래 4:위
area = 0
for i in range(len(lst)):
    if i !=5:
        if lst[i][0] == 1 and lst[i+1][0] == 3:
            area = lst[i][1]*lst[i+1][1]
        elif lst[i][0] == 2 and lst[i+1][0] == 4:
            area = lst[i][1]*lst[i+1][1]
        elif lst[i][0] == 4 and lst[i+1][0] == 1:
            area = lst[i][1]*lst[i+1][1]
        elif lst[i][0] == 3 and lst[i+1][0] == 2:
            area = lst[i][1]*lst[i+1][1]    
        else:
            pass
    else:
        if lst[i][0] == 1 and lst[0][0] == 3:
            area = lst[i][1]*lst[0][1]
        elif lst[i][0] == 2 and lst[0][0] == 4:
            area = lst[i][1]*lst[0][1]
        elif lst[i][0] == 4 and lst[0][0] == 1:
            area = lst[i][1]*lst[0][1]
        elif lst[i][0] == 3 and lst[0][0] == 2:
            area = lst[i][1]*lst[0][1]
        else:
            pass
s = []
g = []
for i in lst:
    if i[0]<3:
        g.append(i[1])
    else:
        s.append(i[1])
a = max(g)*max(s)
final = (a-area)*K
print(final)