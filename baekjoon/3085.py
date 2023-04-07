N = int(input())
candy = [list(map(str,input())) for _ in range(N)]

print(*candy,sep='\n')
print()
candy_rev = list(zip(*candy))
print(*candy_rev, sep='\n')

# 같은 개수 세는 함수
def cnt1():
    k = 0
    l = 0
    cnt = 1
    cnt_lst = []
    while True:
        if k == N:
            break
        if l == N-1:
            k += 1
            l = 0
        elif candy[k][l] == candy[k][l+1]:
            cnt += 1
        elif candy[k][l] != candy[k][l+1]:
            cnt_lst.append(cnt)
            cnt = 1
        l += 1
    return max(cnt_lst)

print(cnt1())
i = 0
j = 0
while True:
    if i == N:
        break
    if j == N-1:
        i+=1
        j = 0
    elif candy[i][j] != candy[i][j+1]:
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        print(cnt1())
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
    j+=1
    



   


