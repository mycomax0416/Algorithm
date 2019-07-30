import sys
sys.stdin = open('4828_sample_input.txt', 'r')

T = int(input())

for j in range(T):
    value_max = 0
    value_min = 1000000
    N = int(input())
    arr = list(map(int, input().split()))


    for i in range(len(arr)):
        if arr[i] > value_max:
            value_max = arr[i]

        if arr[i] < value_min:
            value_min = arr[i]

    print('#{} {}'.format(j+1, value_max - value_min))