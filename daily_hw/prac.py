'''#3-2 과제
year = int(input())

if year % 4 == 0 and not year % 100 == 0:
    print('윤년입니다') 
elif year % 400 == 0:
    print('윤년입니다')
else:
    print('윤년 아닙니다')'''

'''#4-2 과제
words = ["round" , "dream", "magnet" , 
"tweet" , "tweet", "trick", "kiwi"]

for idx in range(len(words)):
    if idx == 4:
        print('tweet 탈락입니다')
    else:
        print(words[idx])
'''

'''#3-4
s_triangle = list(map(int, input().split()))
a = s_triangle[0]
b = s_triangle[1]
c = s_triangle[2]
if a == b == c:
    print('정삼각형')
elif a == b or a == c or b == c:
    print('이등변삼각형')
elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2):
    print('직각삼각형')
elif (a and b < c) and (a + b > c):
    print('삼각형')
elif (a and c < b) and (a + c > b):
    print('삼각형')
elif (c and b < a) and (c + b > a):
    print('삼각형')
else:
    print('삼각형이 아님')
'''

'''#2-2
orders = ['아이스아메리카노','카라멜마키야또','에스프레소','아메리카노','아이스라떼','핫초코','아이스아메리카노','아이스카라멜마키야또','아이스라떼','라떼마키야또','카푸치노']
print(orders)
print(len(orders))
'''

'''#3-4
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
for i in range(len(words)):
    a = 0
    if sorted(words[i]) == sorted(words[i+a]):
        a += 1
        group = words[i] + words[i + a]
        print(group)
    else :
        break
    #print(sorted(words[i]))
    '''
'''#4-1 실습
password = 6278

for i in range(3):
    passtry = int(input())
    if passtry == password:
        print('비밀번호가 맞았습니다')
        break
    else:
        print('비밀번호가 틀렸습니다')
        '''

'''#4-2 실습
students = [
    '박해피',
    '이영희',
    '조민지',
    '조민지',
    '김철수',
    '이영희',
    '이영희',
    '김해킹',
    '박해피',
    '김철수',
    '한케이',
    '강디티',
    '조민지',
    '박해피',
    '김철수',
    '이영희',
    '박해피',
    '김해킹',
    '박해피',
    '한케이',
    '강디티',
]
count = {}
for i in students:
    try: count[i] += 1
    except: count[i] = 1

print(count)'''


'''# 4-3 실습
# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]
num = list(map(int, input().split()))
result = []
for i in num:
    if i not in result:
        result.append(i)
print(result)'''

'''# 4-4 실습
word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')
sum1 = 0
for i in range(len(word1)):
    sum1 = sum1 + ord(word1[i])
    #print(sum1)
sum2 = 0
for i in range(len(word2)):
    sum2 = sum2 + ord(word2[i])
    #print(sum2)
if sum1 > sum2:
    print(word1)
else:
    print(word2)
'''

# 4-5 실습
test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'solving',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'solving',
   	'염자바': 'cheating'
}

for i in test_status.values():
    if i == 'cheating':
        print(test_status.keys)
    else:
        break
#print(test_status)

'''
test = int(input())
test_num = int(input())
grade = map(int, input().split())
count = {}
for i in (grade):
    try: count[i] += 1
    except: count[i] = 1
max_value_key = max(count, key=count.get)
print(max_value_key)
'''



'''t = int(input())
while t:
    #반복횟수를 감소시킴(반복문으로 처리해도 무방함)
    t -= 1
    #몇번째 케이스인지
    case = int(input())
    grade = list(map(int, input().split()))
    lst = [0]*101
    #각 자리수마다 카운팅한다.
    #숫자 1번이 나오면 1번 인덱스에 +1 이런식으로
    for g in grade:
        lst[g] += 1
    #최대값을 찾는다.
    max_num = max(list)
    #최대값과 같은값을 뒤에서부터 찾는다.
    #앞에서 부터 찾으면 정답이 틀릴 수 있다.
    for i in range(100, -1, -1):
        if max_num == lst[i]:
            print(f"#{case} {i}")
            break'''

'''# 5-2 과제

import calendar

while True:
    year = int(input())
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print('윤년입니다. 연도를 다시 입력해주세요')
    else:
        print(calendar.calendar(year))
        break

year1 = int(input())
month1 = int(input())

day1 = int(input())

day = '월화수목금토일'
if day[calendar.weekday(year1, month1, day1)] == '월':
    print('경고 월요일입니다')
print({'년' : year1, '월' : month1, '일' : day1, '요일' : day[calendar.weekday(year1, month1, day1)]})




# def isleap(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    

# print(isleap(year))
'''






    



    
