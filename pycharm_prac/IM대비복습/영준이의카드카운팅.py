T = int(input())
for test_case in range(1, T + 1):
    S = list(map(str, input()))

    card = {'S':[], 'D':[], 'H':[], 'C':[]}
    for i in range(0,len(S),3):
        card[S[i]].append(int(S[i+1])*10 + int(S[i+2]))
    # print(card)

    ans = []
    for val in card.values():
        ans.append(13-len(val))

    for val in card.values():
        for i in val:
            if val.count(i)>1:
                ans = ['ERROR']
                break
    print(f"#{test_case}", *ans)
