# 후위순회
def tree(i):
    if i:
        tree(int(c1[i]))
        tree(int(c2[i]))
        final.append(lst[i-1][1])


for test_case in range(1, 11):
    N = int(input())
    lst = [list(input().split()) for _ in range(N)]
    c1 = [0]*(N+1)
    c2 = [0]*(N+1)

    for i in range(1,len(lst)+1):
        if len(lst[i-1]) > 2:
            if c1[i] == 0:
                    c1[i] = (lst[i-1][2])
            if c1[i] != 0:
                    c2[i] = (lst[i-1][3])
    final = []

    tree(1)
    i = 0
    while i<len(final):
        if final[i] == '-':
            final[i] = int(final[i-2]) - int(final[i-1])
            final.pop(i-2)
            final.pop(i-2)
            i = 0
        elif final[i] == '+':
            final[i] = int(final[i-2]) + int(final[i-1])
            final.pop(i-2)
            final.pop(i-2)
            i = 0
        elif final[i] == '/':
            final[i] = int(final[i-2]) / int(final[i-1])
            final.pop(i-2)
            final.pop(i-2)
            i = 0
        elif final[i] == '*':
            final[i] = int(final[i-2]) * int(final[i-1])
            final.pop(i-2)
            final.pop(i-2)
            i = 0
        i+=1
    print(f"#{test_case} {int(*final)}")



