T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a1 = [[0]*N for _ in range(N)]    # 90도
    a2 = [[0] * N for _ in range(N)]  # 180도
    a3 = [[0] * N for _ in range(N)]  # 270도

    #회전각에 따른 위치 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N - 1 - j][i]
            a2[i][j] = arr[N - 1 - j][N - 1 - j]
            a3[i][j] = arr[j][N - 1 - i]
    print(f"#{test_case}")
    for a, b, c in zip(a1, a2, a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')


'''
a1[i][j] = arr[N-1-j][i]      : 90도
a2[i][j] = arr[N-1-j][N-1-j]  : 180도
a3[i][j] = arr[j][N-1-i]      : 270도 

for a,b,c in zip(a1,a2,a3):
    {"".join(a)}_{"".join(b)}_ 
'''

'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    a1 = [[0] * N for _ in range(N)]  # 90도
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]

    # 회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N - 1 - j][i]
            a2[i][j] = arr[N - 1 - i][N - 1 - j]
            a3[i][j] = arr[j][N - 1 - i]
    print(f'#{test_case}')
    for a, b, c in zip(a1, a2, a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')

'''