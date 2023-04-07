# 5-2 과제

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

