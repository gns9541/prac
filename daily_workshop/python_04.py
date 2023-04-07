#1 간단한 N의 약수

N = int(input())
for i in range(1, N+1):
    if N % i == 0:
        print(i, end = " ")
    else:
        continue

#2 List의 합 구하기

lst = [1 , 2 , 3 , 4 , 5]
def list_sum():
    sum = 0
    for i in lst:
        sum += i
    return(sum)
print(list_sum(lst))

#3 Dictionary 로 이루어진 List 의 합 구하기

lst = [{'name':'kim', 'age': 12}, {'name':'lee', 'age': 4}]
def dict_list_sum():
    add = 0
    for i in lst:
        add += i['age']               
    return(add) 
print(dict_list_sum())

#4 2 차원 List 의 전체 합 구하기

lst = [[1], [2,3], [4,5,6], [7,8,9,10]]
def all_list_sum():
    lst_add = []
    sum = 0
    for i in lst:
        for idx in range(len(i)):
            lst_add.append(i[idx])
    for s in lst_add:
        sum += s
    print(sum) 
    return 

all_list_sum()

#5 ASCII 코드- 숫자의 의미
lst = [83 , 115 , 65 , 102 , 89 ]

def get_secret_word():
    for i in lst:
        print(chr(i), end = "")
    return
get_secret_word()

#6 내 이름은 몇일까?

word = 'happy'
def get_secret_number():
    add = 0
    for i in word:
        add += ord(i)
    print(add)
    return
get_secret_number()

#7 강한이름

word1 = ('z', 'a')
word2 = ('delilah', 'dixon')
def get_strong_word():
    word1_strong = []
    for i in word1:
        word1_strong.append(ord(i))
    print(chr(max(word1_strong)))
    add = 0
    word2_strong = []
    for i in word2:
        for idx in i:
            add += ord(idx)
        word2_strong.append(add)
    print(word2_strong)
    





get_strong_word()









