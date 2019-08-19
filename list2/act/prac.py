# arr = [[9, 20, 2, 18, 11],
# [19, 1, 25, 3, 21],
# [8, 24, 10, 17, 7],
# [15, 4, 16, 5, 6],
# [12, 13, 22, 23, 14]]

# dx = [0, 0, -1, +1]
# dy = [+1, -1, 0, 0]

# X, Y = len(arr), len(arr[0])
# sum = 0

# for x in range(X):
#     for y in range(Y):
#         for i in range(4):
#             tx, ty = x + dx[i], y + dy[i]
#             if tx < 0 or ty < 0 or tx == len(arr) or ty == len(arr[0]):
#                 continue

#             val = arr[x][y] - arr[tx][ty]
#             sum += (-val if val < 0 else val)

# print(sum)
#----------------------------------------------------
arr = [3, 6, -2, 7, -3, 1, -5, -1, 5, 4]
# arr = [3, 6, 7, 1, 5, 4]
N = len(arr)

for i in range(1, 1 << N): # i 는 부분집합을 표현하는 값
    sum = 0
    for j in range(N):
        if i & (1 << j): #arr[k]를 포함하는지 
            sum += arr[j]
    if sum == 0:
        for j in range(N):
            if i & (1 << j): #arr[k]를 포함하는지 
                print(arr[j], end=' ')
        print()    
            
arr = []
key = 123
lo, hi = 0, len(arr) - 1

while lo <= hi:
    mid = (lo+hi) >> 1 # 비트로 나누기 2
    if arr[mid] == key:
        break
    if arr[mid] > key:
        hi = mid - 1
    else:
        lo = mid + 1


#------------------------------
def binarySearch(arr, key):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo+hi) >> 1 # 비트로 나누기 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

#------------------------------
def binarySearch2(arr, lo, hi, key):
    if lo > hi: return False

    mid = (lo + hi) >> 1
    if arr[mid] == key:
        return True
    if arr[mid] > key:
        return binarySearch2(arr, lo, mid - 1, key)
    else:
        return binarySearch2(arr, mid + 1, hi, key)
#-----------------------------------
arr = [64, 25, 10, 22, 11]
N = len(arr)

# [0, n-1] 최소값의 위치를 찾는다.
minIdx = 0
for j in range(minIdx+1, N):
    if arr[minIdx] > arr[j]:
        minIdx = j
arr[0], arr[minIdx] = arr[minIdx], arr[0]
# [1, n-1] 최소값을 찾는다.
minIdx = 1
for j in range(minIdx+1, N):
    if arr[minIdx] > arr[j]:
        minIdx = j
arr[1], arr[minIdx] = arr[minIdx], arr[1]
#[2, n-1]
#[n-2, n-1]
print(arr)

#---------------------------------------
for i in range(N-1):
    minIdx = i
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
print(arr)