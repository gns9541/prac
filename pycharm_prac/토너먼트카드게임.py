# def qsort(i, j, card):
#     # 종료조건
#     if len(card) == 2 or len(card) == 1:
#         return card
#     # 단위작업
#     p = (i+j)//2
#     L = []
#     R = []
#     for k in range(len(card)):
#         if k < p:
#             L.append(card[k])
#         else:
#             R.append(card[k])
#
#     return qsort(0, len(L), L) + ['_'] + qsort(0, len(R), R)

def qsort(s, e):
    if s == e:       # 종료조건
        return s

    a = qsort(s, (s+e)//2)
    b = qsort((s+e)//2+1, e)

    if (card[a]%3)+1 == card[b]:
        return b
    return a


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card = [0]+list(map(int, input().split()))
    ans = qsort(1, N)
    print(f"#{test_case} {ans}")

