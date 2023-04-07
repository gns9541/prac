T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    def msort(lst):
        global cnt
        if len(lst) == 1:
            return lst

        middle = len(lst)//2
        l = lst[:middle]
        r = lst[middle:]
        l = msort(l)
        r = msort(r)

        return m(l,r)

    def m(l,r):
        global cnt
        if l[-1] > r[-1]:
            cnt += 1
        ans = []
        i=0
        j=0
        while len(l)>i or len(r)>j:
            if len(l)>i and len(r)>j:
                if l[i]<= r[j]:
                    ans.append(l[i])
                    i+=1
                else:
                    ans.append(r[j])
                    j+=1
            elif len(l)>i:
                ans.append(l[i])
                i+=1
            elif len(r)>j:
                ans.append(r[j])
                j+=1
        return ans

    print(F"#{test_case} {msort(a)[N//2]} {cnt}")

