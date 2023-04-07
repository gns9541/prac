g, s = map(int, input().split()) # 가로 세로 길이
N = int(input()) # 칼로 자를 점선의 개수
line = [list(map(int, input().split())) for _ in range(N)]
gl = []
sl = []
for lst in line:
    if lst[0] == 0:
        gl.append(lst)
    if lst[0] == 1:
        sl.append(lst)
print(gl)
print(sl)
paper = [[0]*(g+len(sl)) for _ in range(s+len(gl))]
print(*paper, sep="\n")

for j in range(g+len(sl)):
    for i in range(s+len(gl)):
        for idx in gl:
            if idx[1] == j:
                paper[j][i] == 1
print(*paper, sep="\n")


