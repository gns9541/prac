grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
lst = []
for i in grain_lst:
    i = list(i)
    lst.append(i)
price = []
for idx in lst:
    price.append(idx[1])
max_price = max(price)
for max in lst:
    if max[1] == max_price:
        print(max[0])

