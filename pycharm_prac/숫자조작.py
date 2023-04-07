# 재귀 버려
'''
def mx(i):
    global ans
    if i == len(N):
        ans.append(N)
        return
    elif N[i] != n_new[-1-i]:
        for k in range(len(N)):
            if N[k] == n_new[-1-i]:
                N[i], N[k] = N[k], N[i]
                ans.append(N)
                return

    else:
        mx(i+1)


def mn(j):
    if j == len(N_mx):
        ans1.append(N_mx)
        return
    elif N_mx[j] != n_new[0+j] and N_mx[j] != 0 and n_new[0+j] != 0:
        for k in range(len(N_mx)):
            if N_mx[k] == n_new[0+j]:
                N_mx[j], N_mx[k] = N_mx[k], N_mx[j]
                ans1.append(N_mx)
                return
    else:
        mn(j+1)


T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int, input()))
    n_new = sorted(N)
    N_mx = []
    for k in N:
        N_mx.append(k)
    ans = []
    ans1 = []
    mn(0)
    mx(0)
    ans1 = sum(ans1,[])
    ans = sum(ans,[])
    ans1="".join(map(str,ans1))
    ans = "".join(map(str, ans))
    print(f"#{test_case}",ans1, ans)
'''
# N개 중에 2개 뽑는 모든 조합 코드 사용하기
# 모두 해보고 가장 좋은 값 저장
# N개에서 3개뽑기?
N = [1,2,3,4,5,6]
for i in range(len(N)-2):
    for j in range(i+1,len(N)-1):
        for k in range(j+1, len(N)):
            print(N[i],N[j],N[k])



