num_list = [4, 4, 7, 8, 10, 4]

def sum_of_repeat_number(num_list):
    sum = 0    
    for i in num_list:
        num = num_list.count(i)
        if num == 1:
            sum += i
        else:
            continue
    return(sum)
        
print(sum_of_repeat_number(num_list))


