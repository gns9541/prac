N = int(input())
sit = list(input())

cup = 1
cnt = 0
for i in sit:
    if i == 'S':
        cup += 1
    else:
        cnt+=1
        if cnt ==2:
            cup += 1
            cnt = 0
if len(sit) >= cup:
    print(cup)
else:
    print(len(sit))
