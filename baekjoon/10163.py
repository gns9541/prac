N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# print(*paper, sep='\n')
arr = [['.']*1002 for _ in range(1002)] # (j, i)

for k in range(len(paper)):
    for j in range(paper[k][2]): # x좌표
        for i in range(paper[k][3]): #y좌표
            arr[paper[k][1]+i][paper[k][0]+j] = k
    # print(*arr, sep="\n")
for k in range(N):
    ans = 0
    for lst in arr:
        ans += lst.count(k)
    print(ans)

