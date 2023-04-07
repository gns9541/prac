# for test in range(10):
T = int(input())
pattern = input()
text = list(input())
M = len(pattern)
N = len(text)
cnt = 0

# for i in range(N-1):
#     for j in range(M):
#         if text[i+j] == pattern[j]:
#             cnt +=1
# print(cnt)

i = 0
j = 0
cnt = 0
while j < M and i < N:
    if text[i] != pattern[j]:
        i = i-j
        j = -1
    # elif text[i] == pattern[j]:
    #     cnt +=1
    i = i+1
    j = j+1
if j == M:
    print(i - M)
else:
    print(0)





