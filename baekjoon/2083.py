# people = [input().split() for _ in range()]
# print(people)
# for i in people:
#     if int(i[1]) > 17:
#         print(i[0], "Senior")
#     elif 0 < int(i[1]) <= 16:
#         print(i[0], "Junior")
#     elif int(i[2]) >= 80:
#         print(i[0], "Senior")
#     elif 0 < int(i[2]) < 80:
#         print(i[0], "Junior") 
#     elif int(i[1]) == 0 or int(i[2]) == 0:
#         pass

people =""
lst = []
while True:
    people = input().split()
    lst.append(people)

    if people == ["#", "0", "0"]:
        break
    
lst.remove(["#", "0", "0"])

for i in lst:
    if int(i[1]) > 17 or int(i[2]) >= 80:
        print(i[0], "Senior")
    elif 0 < int(i[1]) <= 16 or 0 < int(i[2]) < 80:
        print(i[0], "Junior")
    # elif int(i[1]) == 0 or int(i[2]) == 0:
    #     pass
# print(lst)




# for i in lst:
#     if int(i[1]) > 17:
#             print(i[0], "Senior")
#     elif 0 < int(i[1]) <= 16:
#             print(i[0], "Junior")
#     elif int(i[2]) >= 80:
#             print(i[0], "Senior")
#     elif 0 < int(i[2]) < 80:
#             print(i[0], "Junior") 
#     elif int(i[1]) == 0 or int(i[2]) == 0:
#         pass
    





