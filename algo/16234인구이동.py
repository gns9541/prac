N,L,R = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
print(*P, sep="\n")
print()
ans = 0
while True:
    st = []
    cnt = 0
    for i in range(N):
        for j in range(len(P[0])-1):
            if L<=abs(P[i][j]-P[i][j+1])<=R:
                if [i,j] not in st:
                    cnt += P[i][j]
                    st.append([i,j])
                if [i,j+1] not in st:
                    cnt+=P[i][j+1]
                    st.append([i,j+1])
            
    for j in range(len(P[0])):
        for i in range(N-1):
            if L<=abs(P[i][j]-P[i+1][j])<=R:
                if [i,j] not in st:
                    cnt += P[i][j]
                    st.append([i,j])
                if [i+1,j] not in st:
                    cnt+=P[i+1][j]
                    st.append([i+1,j])
    if cnt == 0:
        break
    else:
        for i in range(N):
            for j in range(len(P[0])):
                if [i,j] in st:
                    P[i][j] = cnt//len(st)
    ans += 1
    print(st)
    print(cnt)
    print(*P, sep="\n")
    print(ans)
        
