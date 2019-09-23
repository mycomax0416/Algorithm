arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)
def mergeSort(lo, hi):
    # print(lo, hi)        # 매개변수 --> 문제의 크기
    if lo == hi:
        return

    # 분할
    mid = (lo+hi) >> 1
    mergeSort(lo, mid)      # 왼쪽
    mergeSort(mid+1, hi)    # 오른쪽
    # 왼쪽과 오른쪽을 병합
    i, j, k = hi-1, mid, hi-1
    while lo <= j and mid+1 <= i:
        if arr[j] < arr[i]:
            tmp[k] = arr[i]
            i -= 1
            k -= 1
        else:
            tmp[k] = arr[j]
            j -= 1
            k -= 1

    while mid+1 <= i:
        tmp[k] = arr[i]
        i -= 1
        k -= 1

    while lo <= j:
        tmp[k] = arr[j]
        j -= 1
        k -= 1

    for i in range(lo, hi+1):
        arr[i] = tmp[i]

print(arr)
mergeSort(0, len(arr)-1)
print(arr)
