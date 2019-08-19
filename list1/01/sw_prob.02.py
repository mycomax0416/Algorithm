import sys
sys.stdin = open('input.txt', 'r')

for j in range(10):

    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    right_max = 0
    left_max = 0
    total_max = 0

    for i in range(2, len(arr)-2):
        if arr[i-2] > arr[i-1]:
            left_max = arr[i-2]
        else:
            left_max = arr[i-1]
        if arr[i+1] > arr[i+2]:
            right_max = arr[i+1]
        else:
            right_max = arr[i+2]
        if left_max > right_max:
            total_max = left_max
        else:
            total_max = right_max
        if arr[i] > total_max:
            count += (arr[i]-total_max)

    print('#{} {}'.format(j+1, count))