# for test_case in range(1, 11):
Dn = int(input())
box = list(map(int, input().split()))
# print(box)

while Dn > 0:
    for i in range(len(box)-1, 0, -1):
        for j in range(0, i):
            if box[j] > box[j+1]:
                box[j], box[j+1] = box[j+1], box[j]
    # print(box)
    box[-1] = box[-1]-1
    box[0] = box[0]+1
    
    print(box)
    if Dn < 0:
        print(box[-1] - box[0])
        break
    if box[0] == box[-1] or box[0] == box[-1]:
        print(box[-1]-box[0])
        break
    Dn -= 1

print(box[-1]-box[0])


for test_case in range(1, 11):
    Dn = int(input())
    box = list(map(int, input().split()))
 
    while Dn > 0:
        for i in range(len(box)-1, 0, -1):
            for j in range(0, i):
                if box[j] > box[j+1]:
                    box[j], box[j+1] = box[j+1], box[j]
         
         
        if Dn < 0:
            print(f"#{test_case} {box[-1]-box[0]}")
            break
        if box[0] == box[-1] or box[0] == box[-1]:
            print(f"#{test_case} {box[-1]-box[0]}")
            break
 
        Dn -= 1
        box[-1] = box[-1]-1
        box[0] = box[0]+1
        for i in range(len(box)-1, 0, -1):
            for j in range(0, i):
                if box[j] > box[j+1]:
                    box[j], box[j+1] = box[j+1], box[j]
 
    print(f"#{test_case} {box[-1]-box[0]}")





# 5 8 3 1 5 6 9 9 2 2 4