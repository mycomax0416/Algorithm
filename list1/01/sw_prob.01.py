import sys
sys.stdin = open('input.txt', 'r')

for j in range(10):

    N = int(input())
    arr = list(map(int, input().split()))

    # print(N, arr)

    count = 0

    for i in range(2, len(arr)-2):
        tall = max([arr[i-2], arr[i-1], arr[i+1], arr[i+2]])
        if arr[i] > tall:
            count += (arr[i]-tall)
    # print(count)

    print('#{} {}'.format(j+1, count))