import random

height = [int(input()) for _ in range(9)]
# height_int = list(map(int,(height)))
# print(height)

sum = sum(height)
# print(sum)
     
   
if sum > 100:
    while True:
        false = random.sample(height,2)
        if false[0] + false[1] == sum - 100:
            height.remove(false[0])
            height.remove(false[1])
            height.sort()
            break
        else: 
            continue

for i in height:
    print(i)
        

