S = list(input().split())
for i in S:
    i = list(i)
    i_rev = i[::-1]
    final = "".join(i_rev)
    print(final, end = " ")


for i in S:
    i = list(i)
    lst = []
    for j in range(len(i)):
        if i[j] == '<':
            while True:
                lst.append(i[j])
                j += 1
                if i[j] == '>':
                    lst.append(i[j])
                    break
    for j in lst:
        i.remove(j)
    i_rev = i[::-1]
print(lst)
print(i_rev)






