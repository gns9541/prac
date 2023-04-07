N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]
# print(p)

x = []
y = []
for i in range(0, 100):
    x.append(i)
    y.append(i)

paper = []
for i in range(100):
    for j in range(100):
        paper.append((x[i],y[j]))
# print(paper)
cnt = 0
for j in range(len(p)):
    x1=[]
    y1=[]
    for i in range(0, 11):
        x1.append(p[j][0]+i)
        y1.append(p[j][1]+i)

    # print(x1,y1)
    pf = []
    for i in (x1):
        for j in y1:
            pf.append((i,j))
    # print(pf)

    # cnt = 0
    for j in pf:
        for i in paper:
            if i == j:
                paper.remove(i)
                cnt += 1
            if j not in paper:
                pass

    print(cnt)
    print(paper)