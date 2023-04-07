K = int(input())
lenth = [list(map(int,input().split())) for _ in range(6)]
# print(*lenth, sep="\n")
s = []
g = []
for i in lenth:
    if i[0]<3:
        g.append(i[1])
    else:
        s.append(i[1])
sq = max(g)*max(s)

ans = 0
for i in range(len(lenth)-2):
    if i != 3 and lenth[i][0] == lenth[i+2][0] and lenth[i+1][0] == lenth[i+3][0]:
        ans = sq - lenth[i+1][1]*lenth[i+2][1]
        break
    elif i == 3 and lenth[i][0] == lenth[i+2][0] and lenth[i+1][0] != lenth[i-1][0]:
        ans = sq - lenth[i+1][1]*lenth[i+2][1]
        break
    elif i != 0 and lenth[i][0] == lenth[i+2][0] and lenth[i+1][0] == lenth[i-1][0]:
        ans = sq - lenth[i][1]*lenth[i+1][1]
        break
    elif i == 0 and lenth[i][0] == lenth[i+2][0] and lenth[i+1][0] != lenth[i-1][0]:
        ans = sq - lenth[i][1]*lenth[i+1][1]
        break
    elif i == 0 and lenth[i][0] == lenth[-2][0]:
        ans = sq - lenth[i][1]*lenth[-1][1]
print(ans*K)









    