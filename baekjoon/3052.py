lst = []
st = []
for _ in range(10):
    num = int(input())
    lst.append(num%42)

i = 1
st.append(lst[0])
while True:
    if i == 10:
        break
    if lst[i] not in st:
        st.append(lst[i])
        i+=1
    else:
        i += 1
print(len(st))