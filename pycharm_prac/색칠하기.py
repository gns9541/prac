# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
lst = [[0]*10 for _ in range(10)]
N = int(input())
red = []
blue = []
for i in range(N):
    color = list(map(int, input().split()))
    if color[-1] == 2:
        blue.append(color)
    else:
        red.append(color)
        
print(red)
print(blue)
for i in range(len(red)):
    while True:
        lst[red[i][0]][red[i][1]]
    