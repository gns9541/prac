N = int(input())
lst3 = []
lst5 = []
for i in range(1, N+1):
    if i %3 == 0:
        lst3.append(i)
    if i%5 == 0:
        lst5.append(i)
# print(lst3, lst5)
ans = []
for i in range(len(lst3)):
    if lst3[i] == N:
        ans.append(i+1)
for j in range(len(lst5)):
    if lst5[j] == N:
        ans.append(j+1)
for i in range(len(lst3)):
    for j in range(len(lst5)):   
        if lst3[i]+lst5[j] == N:
            ans.append(i+1+j+1) 
        
         
# print(ans)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))