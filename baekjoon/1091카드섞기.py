N = int(input()) #카드개수
P = list(map(int, input().split())) # 최종 카드 위치 사람 수
S = list(map(int, input().split())) # 카드 섞는 방법

final = [0]*3
num = []

for i in range(N):
    num.append(i)

for i in range(len(num)):
    final[P[i]] = num[i]
print(num)
print(final)
print()
cnt = 0
while True:
    if cnt ==3:
        break
    new_num = [0]*3
    for i in range(len(num)):
        new_num[i] = num[S[i]]
        print(new_num)
        num = new_num
        
    cnt += 1




# print(S)
# print(P)

