L, P = map(int,input().split())
n1, n2, n3, n4, n5 = map(int,input().split())
lst_n = [n1, n2, n3, n4, n5]
real = L * P
for i in lst_n:
    print(i - real, end=" ")
