# 거품 정렬

arr = [55, 7, 78, 12, 42]
n = len(arr)
for j in range(n-1, 0, -1):
    for i in range(j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)

MIN = arr[0]
for i in range(1, len(arr)):
    if arr[i] < MIN:
        MIN = arr[i]

print(MIN)

# 선택정렬

for j in range(len(arr)-1):
    MIN = j

    for i in range(j+1, len(arr)):
        if arr[i] < arr[MIN]:
            MIN = i
    arr[j], arr[MIN] = arr[MIN], arr[j]

print(arr)


data = [0, 3, 1, 3, 1, 2, 4, 1]
counts = [0] * 5 # 최대값 = 4

for val in data:
    counts[val] += 1

# for i in range(1. len(counts)):
#     counts[i] = counts[i-1] + counts[i]

# sorted = []
# for i in range(len(counts)):
#     for j in range(counts[i]):
#         # sorted += [i]
#         sorted.append(i)
    

# print(sorted)

data = 'ABC'

n = len(data)
for i in range(n):
    for j in range(n):
        if i == j: 
            continue
        for k in range(n):
            if i == k or j == k: 
                continue
            print(data[i], data[j], data[k])

