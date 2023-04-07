def quicksort(arr, l, r):
    def partition(l, r):
        pivot = arr[r]
        left = l # 값의 시작 범위
        for right in range(l, r):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
        arr[left], arr[r] = arr[r], arr[left]
        return left

    if l < r:
        s = partition(l, r)
        quicksort(arr, l, s - 1)
        quicksort(arr, s + 1, r)

    return arr[N//2]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    l = 0
    r = len(A) - 1
    ans = quicksort(A, l, r)
    print(f"#{test_case} {ans}")
