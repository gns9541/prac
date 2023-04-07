import collections

entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

count_entry = collections.Counter(entry_record)
count_exit = collections.Counter(exit_record)

lst_num = []
for people in count_entry.items():
    lst_num.append(people)
    lst_num.sort(key = lambda x: x[1])
# print(lst_num)
people1 = lst_num[-1]
people2 = lst_num[-2]
people3 = lst_num[-3]
print("입장 기록 많은 Top3\n"f"{people1[0]} {people1[1]}회\n"
f"{people2[0]} {people2[1]}회\n"
f"{people3[0]} {people3[1]}회")


print("\n출입 기록이 수상한 사람")
for key in count_entry.keys():
    if count_entry.get(key) == count_exit.get(key):
        pass
    if count_entry.get(key) > count_exit.get(key):
        print(f"{key}은 입장기록이 {(count_entry.get(key))-(count_exit.get(key))}회 더 많아 수상합니다.")
        continue
    if count_entry.get(key) < count_exit.get(key):
        print(f"{key}은 퇴장기록이 {(count_exit.get(key))-(count_entry.get(key))}회 더 많아 수상합니다.")


    



