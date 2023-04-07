lst = []
while True:
    N = input().split()
    lst.append(N)

    if N == ["0"]:
        break
lst.remove(["0"])
# print(lst)


for i in lst:
    
    for idx in i:
        sum = 0
        # print(idx)
        for index in idx:
            if int(index) == 1:
                sum += 2  
            elif 2 <= int(index) <=9:
                sum += 3
            elif int(index) == 0:
                sum += 4
    print(sum + len(idx)-1 + 2)
