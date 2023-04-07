word = input()
N = len(word)
lst = []
for i in range(N+1):
    for j in range(i+1,N+1):
        if i*j == N:
            lst.append([i,j])
R = max(lst)[0] #세로길이
C = max(lst)[1] #가로길이

arr = [[0]*C for _ in range(R)]


for k in word:
    
    for j in range(C):
        for i in range(R):
            if arr[i][j] == 0:
                arr[i][j] = k
                break
        
                # print(*arr, sep="\n")
                
           
print(*arr, sep="\n")

