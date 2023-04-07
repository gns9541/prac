num = [input().split() for _ in range(10)]

people_go = 0
lst_people_go = []
for i in num:
    people = -(int(i[0])) + int(i[1])
    people_go += people
    lst_people_go.append(people_go)
    
    # print(people)
    # print(people_go)
print(max(lst_people_go))