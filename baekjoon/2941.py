word = list(map(str, input()))
print(word)
dic = {'c1':'c=', 'c2':'c-', 'dz':'dz=', 'd':'d-', 'lj':'lj', 'nj':'nj', 's':'s=', 'z':'z='}
st = []
cnt = 0
i = 0
while True:
    if len(word) == 0:
        break
    if len(word) == 1:
        cnt += 1
        st.append(word.pop(i))
        st.append('_')

    elif len(word) == 2:
        if word[i]+word[i+1] in dic.values():
            st.append(word.pop(i))
            st.append(word.pop(i))
            st.append('_')
        else:
            st.append(word.pop(i))
            st.append('_')
        cnt +=1

    elif word[i]+word[i+1] in dic.values():
        cnt +=1
        st.append(word.pop(i))
        st.append(word.pop(i))
        st.append('_')

    elif word[i]+word[i+1]+word[i+2] in dic.values():
        cnt += 1
        st.append(word.pop(i))
        st.append(word.pop(i))
        st.append(word.pop(i))
        st.append('_')
        
    else:
        cnt += 1
        st.append(word.pop(i))
        st.append('_')
print(st) 
print(cnt)

