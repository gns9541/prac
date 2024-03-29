# C = int(input())
# N = int(input())
# cn = [list(map(int, input().split())) for _ in range(N)]

def dfs_stk(start):
    v = [0] * (V + 1)
    stk = []

    s = start
    v[s] = 1
    alst.append(s)

    while True:
        # s에서 연결된, 미방문의 노드 발견시 이동! (번호순)
        for e in range(1, V + 1):
            if v[e] == 0 and adj[s][e]:
                stk.append(s)  # 주의: 되돌아올 위치(지금 기준점: s)를 push!

                s = e
                v[s] = 1
                alst.append(s)
                break  # 찾았으면 즉시, 그곳을 기준으로 탐색
        else:  # 더 이상 연결된 방문노드 없는 경우 => 막다른길..!
            if stk:
                s = stk.pop()  # 스택에서 꺼낸 최근 기준점이 바로 기준
            else:
                break  # 더이상 탐색할 기준점 없음


V = int(input()) 
E = int(input())
# [1] 연결행렬에 연결표시(1)
adj = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    s, e = map(int, input().split())
    adj[s][e] = adj[e][s] = 1

# print(*adj, sep="\n")
alst = []
dfs_stk(1)
print(len(alst)-1)
