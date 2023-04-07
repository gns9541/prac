num = list(map(int, input().split()))
i = 0
num1 = sorted(num)

while True:
    if i == 4:
        if num == num1:
            break
        else:
            i = 0
    elif num[i]>num[i+1]:
        num[i], num[i+1] = num[i+1], num[i]
        i+=1
        print(*num)
    elif num[i]<num[i+1]:
        i+=1
    
   
    
    