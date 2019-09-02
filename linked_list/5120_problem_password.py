import sys
sys.stdin = open('5120_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    pre = 0
    result = ''

    for k in range(K):
        if pre + M < len(arr):
            pre += M
            arr.insert(pre, arr[pre-1] + arr[pre])
        
        elif pre + M == len(arr):
            pre += M
            arr.append(arr[-1] + arr[0])

        else:
            pre = pre + M - len(arr)
            arr.insert(pre, arr[pre-1]+arr[pre])

    if len(arr) < 10:
        for _ in range(len(arr)):
            result += ' ' + str(arr.pop())

    else:
        for _ in range(10):
            result += ' ' + str(arr.pop())

    print('#{}{}'.format(t+1, result))