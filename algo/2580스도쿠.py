S = [list(map(int, input().split())) for _ in range(9)]
N = 0
for i in range(9):
    for j in range(9):
        if S[i][j] == 0:
            N += 1

def line1(i,j):
    for k in range(9):
        if S[i][k] == j:
            False
        else:
            True
    for k in range(9):
        if S[k][j] == i:
            False
        else:
            True
def box(i,j):
    for 


def dfs(i,cnt):
    if cnt == N:
        return
    pass

dfs(,cnt)
