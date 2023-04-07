T = int(input())
for test_case in range(1, T + 1):
    word = input()
    stack = []
    for i in word:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    print(f"#{test_case} {len(stack)}")



    # for i in range(0,len(word)-1):
    #     stack.append(word[i])
    #     print(stack)
    #     if stack[-1] == word[i+1]:
    #         stack.pop()
    #         word.remove()


