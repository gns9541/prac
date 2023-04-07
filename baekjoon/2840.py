N, K = map(int, input().split()) # 칸수, 돌리는 횟수
lst = [0]*N
word_lst = []
i = 0 
cnt = 0 
while True:
    if cnt == K:
        break
    S, word = map(str, input().split())
    word_lst.append(word)

    if 0<= i-int(S) <N:
        if lst[i-int(S)] == 0:
            lst[i-int(S)] = word
            i = i-int(S) 
        
    else:
        if int(S) >= N:
            if lst[i-int(S)%N] == 0:
                lst[i-int(S)%N] = word
                i = i-int(S)%N
        else:
            if N-int(S)+i >= N:
                if lst[i-int(S)] == 0:
                    lst[i-int(S)] = word
                    i = i-int(S)
            else:
                if lst[N-int(S)+i] == 0:
                    lst[N-int(S)+i] = word
                    i = N-int(S)+i
    cnt += 1
    # print(i)
# print(lst)
# print(word_lst)
ans = 0
for l in word_lst:
    if l not in lst:
        ans = '!'
if word_lst == lst:
    ans = '!'
if ans != '!':
    final = []
    j = lst.index(word_lst[-1])
    while True:
        if len(final) == len(lst):
            break
        if j > len(lst)-1:
            j = 0
        final.append(lst[j])
        j+=1
    for k in range(len(lst)):
        if final[k] == 0:
            final[k] = '?'
    ans = final
print("".join(ans))
    