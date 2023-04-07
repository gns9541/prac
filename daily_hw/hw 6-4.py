# 6-4 과제
words = input().split()
def groupan_agrams(words):
    dic = {}
    for i in words:
        key = "".join(sorted(i))  

        if key not in dic.keys():   
            dic[key] = [i]       
        else:
            dic[key].append(i)    

    return list(dic.values())    
print(groupan_agrams(words))



