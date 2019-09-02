import sys
sys.stdin = open('6485_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    count = [0 for _ in range(5001)]
    result = ''

    for n in range(N):
        a, b = map(int, input().split())
        for idx in range(a, b+1):
            count[idx] += 1

    idxs = []
    P = int(input())

    for p in range(P):
        idxs.append(int(input()))

    for idx in idxs:
        result += ' ' + str(count[idx])

    print('#{}{}'.format(t+1, result))
