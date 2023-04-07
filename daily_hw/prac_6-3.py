def count_vowels(word):
    cnt = 0
    for i in word:
        if i in ['a','e','o','i','u']:
            cnt += 1
    print(cnt)
    return 


count_vowels('apple') #=> 2
count_vowels('banana') #=> 3