square = [list(map(int, input().split())) for _ in range(4)]
lst = [[0]*100 for _ in range(100)] 
for i in square:
    for x in range(i[0], i[2]):
        for y in range(i[1], i[3]):
            lst[x][y] = 1
ans = 0
for i in lst:
    for j in i:
        if j == 1:
            ans += 1

# print(*lst, sep="\n")
print(ans)
    