def quicksort(lst):
    # 종료조건부터 만들기
    if len(lst) < 2: # 정렬할 요소가 1개라면 종료해
        return lst
    # 단위작업 해주기 : p기준으로 좌우분리
    p = lst.pop()
    L = []
    R = []
    for n in lst:
        if n < p:
            L.append(n)
        else:
            R.append(n)
    # 왼 정렬한 결과 + [p] + 오른쪽 정렬 결과
    return quicksort(L) + [p] + quicksort(R)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = quicksort(lst)
    ans = lst[N//2]
    print(f"#{test_case} {ans}")
    # a.sort()

