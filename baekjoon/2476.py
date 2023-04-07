N = int(input())
people = [input().split() for _ in range(N)]

# print(N)
# print(people)

lst_price = []
for i in people:
    if int(i[0]) == int(i[1]) == int(i[2]):
        price = 10000 + int(i[0])*1000
    elif int(i[0]) != int(i[1]) != int(i[2]):
        lst = [int(i[0]), int(i[1]), int(i[2])]
        price = max(lst)*100
    elif int(i[0]) == int(i[1]):
        price = 1000 + int(i[0])*100
    elif int(i[0]) == int(i[0]):
        price = 1000 + int(i[0])*100
    elif int(i[1]) == int(i[2]):
        price = 1000 + int(i[1])*100
    
    lst_price.append(price)

print(max(lst_price))



    
