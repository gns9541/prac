score = [int(input()) for _ in range(10)]
# print(score)
sum = 0
sum_lst = []
for i in range(10):
    sum += score[i]
    sum_lst.append(sum)
    if sum > 100:
        break
# print(sum_lst)
if len(sum_lst) == 1:
    print(sum_lst[0])
else:
    if sum_lst[-1] - 100 <= 100 - sum_lst[-2]:
        print(sum_lst[-1])
    else:
        print(sum_lst[-2])


