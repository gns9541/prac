today = "2022.02.28"
terms = ["A 23"]
privacies = ["2020.01.28 A"]

def year(a):
    return [int(a[0]+a[1]+a[2]+a[3]), int(a[5]+a[6]), int(a[8]+a[9])]
print(year(today))
# print(terms[0][2])
ans = []
for i in range(len(privacies)):
    for j in range(len(terms)):
        if privacies[i][-1] == terms[j][0]:
            # 년도 안바뀔 때
            lst = []
            if len(terms[j]) == 4:
                p = 10+int(terms[j][3])+(int(privacies[i][5])*10+int(privacies[i][6]))
                if p <= 12:
                    lst=year(privacies[i])
                    lst[1] = p
                elif 12<p<24:
                    lst=year(privacies[i])
                    lst[0]+=p//12
                    lst[1] += p%12
                else:
                    lst=year(privacies[i])
                    lst[0]+=(p-12)//12
                    lst[1] += p%12
            else:
                p = (int(terms[j][2])+int(privacies[i][5])*10+int(privacies[i][6]))
                if p <= 12:
                    lst=year(privacies[i])
                    lst[1] = p
                elif 12<p<24:
                    lst=year(privacies[i])
                    lst[0]+=p//12
                    lst[1] += p%12
                else:
                    lst=year(privacies[i])
                    lst[0]+=(p-12)//12
                    lst[1] += p%12
            print(lst)

            if year(today)[0]>lst[0]:
                ans.append(i+1)
            else:
                if year(today)[1]>lst[1]:
                    ans.append(i+1)
                elif year(today)[1]<lst[1]:
                    break
                else:
                    if year(today)[2]>=lst[2]:
                        ans.append(i+1)
print(ans)