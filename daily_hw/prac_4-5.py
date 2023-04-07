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

for i in test_status.keys():
    if test_status[i] == 'cheating':
        
        print([i])
    else:
        continue


del test_status['최이썬']
del test_status['임온실']
del test_status['염자바']
print(test_status)