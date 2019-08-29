import sys
sys.stdin = open('5097_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for m in range(M):
        out = arr.pop(0)
        arr += [out]

    print('#{} {}'.format(t+1, arr[0]))
