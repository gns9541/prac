P = int(input())
lst = [list(map(int, input().split())) for _ in range(P)] # 테스트, 키
    
for k in lst:
    st = [k[1]]
    cnt = 0
    for i in range(2,len(k)):
        cnt1 = 0
        for j in range(len(st)):
            if st[j] > k[i]:
                st.insert(j, k[i])
                cnt += len(st)-(j+1)
                break
            else:
                if cnt1 == len(st)-1:
                    st.append(k[i])
                    break
            cnt1 += 1
    print(k[0], cnt)
    
