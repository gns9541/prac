from collections import deque

def bfs(s,e):
    v=[0]*(1000001)
    q=deque()
    v[s]=1
    q.append(s)
    while q:
        c = q.popleft()
        if c==e:
            return v[e]-1
        for t in ((c+1),(c-1),(c*2),(c-10)):
            if 1<=t<=1000000 and v[t]==0:
                q.append(t)
                v[t]=v[c]+1


T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    ans = bfs(N,M)
    print(f"#{test_case} {ans}")




