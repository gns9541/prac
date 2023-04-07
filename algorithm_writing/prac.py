def perm1(i,k):               
    if i == k:
      print(*p1)
    else:
      for j in range(i, k): # 자신부터 오른쪽 원소들과 교환
        p1[i], p1[j] = p1[j], p1[i]
        perm1(i+1, k)
        p1[i], p1[j] = p1[j], p1[i]

p1 = [1,2,3]
perm1(0,3)

print('####################################################')

def perm2(i,k):
   if i == k:
      print(*p2) # 사전 순으로 나열
   else:
      for j in range(k):
         if used[j] == 0:
            p2[i] = A[j]
            used[j] = 1 # 숫자사용 표시
            perm2(i+1,k)
            used[j] = 0 # 초기화

A = [1,2,3]
p2 = [0]*3
used = [0]*3
perm2(0,3)
print()
##########################################################

def ncr(n,r,s): # n개에서 r개를 고르는 조합, s 선택할 수 있는 구간의 시작
    if r == 0:
      print(*comb)
    else:
      for i in range(s,n-r+1):
        comb[r-1] = A[i]
        ncr(n, r-1, i+1)

n = 10
r =3
comb = [0]*3
A = [i for i in range(n)]
ncr(n,r,0)
print()
##########################################
def f(i,k):
   if i == k:
      print(bit)
   else:
      bit[i] = 0
      f(i+1, k)
      bit[i] = 1
      f(i+1, k)

A = [7,2,5,3,4]
N = len(A)
bit = [0]*N # bit[i] A[i]원소가 부부닙합에 포함되는지 표시
f(0,N)