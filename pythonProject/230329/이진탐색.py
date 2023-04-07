T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()

    ans = 0
    def binary_search(arr, target, start, end):
        global ans
        flag = 2
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                ans += 1
                return
            elif arr[mid] > target:
                end = mid - 1
                if flag == 1:
                    break
                flag = 1
            else:
                start = mid + 1
                if flag == 0:
                    break
                flag = 0
        return

    n = len(A)
    flag = 2
    for i in B:
        binary_search(A, i, 0, n - 1)

    print(f"#{test_case} {ans}")
