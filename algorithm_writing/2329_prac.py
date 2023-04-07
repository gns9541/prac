# def merge(left, right):
#     pass



# def msort(arr):
#     if len(arr) == 1:
#         return arr
#     # left = []
#     # right = []
#     middle = len(arr)//2
#     # for x in range(arr[0:middle+1]):
#     #     left.append(arr[x])
#     # for x in range(arr[middle:]):
#     #     right.append(arr[x])

#     left = arr[0:middle]
#     right = arr[middle:]
    
#     left = msort(left)
#     right = msort(right)

#     return merge(left, right)


# N = int(input())
# arr = list(map(int, input().split()))
# tmo = [0]*N
# msort(arr)

###################################################################

def msort(s,e):
    if s==e:
        return
    m = (s+e)//2
    msort(s,m)
    msort(m+1,e)

    # merge()
    k=0
    l,r = s,m+1 # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while l<=m or r<=e:
        if l<=m and r<=e:
            if arr[l] <= arr[r]:
                tmp[k] = arr[l]
                l += 1
            else:
                tmp[k] = arr[r]
                r += 1
            k += 1
        elif l<=m:
            while l<=m:
                tmp[k] = arr[l]
                l += 1
                k += 1
        elif r<=e:
            while r<=e:
                tmp[k] = arr[r]
                r += 1
                k += 1
    i = 0
    while i<k:
        arr[s+i] = tmp[i] 
        i += 1
    return arr

N = int(input())
arr = list(map(int, input().split()))
tmp = [0]*N
print(msort(0,N-1))

