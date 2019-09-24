arr = [69, 10, 30, 2, 16, 8, 31, 22]
# tmp = [0] * len(arr)
# def mergeSort(lo, hi):
#     # print(lo, hi)        # 매개변수 --> 문제의 크기
#     if lo == hi:
#         return

#     # 분할
#     mid = (lo+hi) >> 1
#     mergeSort(lo, mid)      # 왼쪽
#     mergeSort(mid+1, hi)    # 오른쪽
#     # 왼쪽과 오른쪽을 병합
#     i, j, k = lo, mid+1, lo
#     while i <= mid and j <= hi:
#         if arr[i] < arr[j]:
#             tmp[k] = arr[i]
#             i += 1
#             k += 1
#         else:
#             tmp[k] = arr[j]
#             j += 1
#             k += 1

#     while i <= mid:
#         tmp[k] = arr[i]
#         i += 1
#         k += 1

#     while j <= hi:
#         tmp[k] = arr[j]
#         j += 1
#         k += 1

#     for i in range(lo, hi+1):
#         arr[i] = tmp[i]

# print(arr)
# mergeSort(0, len(arr)-1)
# print(arr)
#-------------------------------------
def quickSort(lo, hi):
    if lo >= hi:
        return

    i, j, pivot = lo, hi, arr[lo]

    while i < j:
        while i <= hi and pivot >= arr[i]:
            i += 1
        while pivot < arr[j]:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[lo], arr[j] = arr[j], arr[lo]

    quickSort(lo, j-1)
    quickSort(j+1, hi)

print(arr)
quickSort(0, len(arr)-1)
print(arr)
#------------------------------------------
# def quickSort(lo, hi):
#     if lo >= hi:
#         return
#     i = lo - 1

#     for j in range(lo, hi):
#         if arr[hi] >= arr[j]:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     i += 1
#     arr[hi], arr[i] = arr[i], arr[hi]

#     quickSort(lo, i - 1)
#     quickSort(i + 1, hi)

# print(arr)
# quickSort(0, len(arr)-1)
# print(arr)