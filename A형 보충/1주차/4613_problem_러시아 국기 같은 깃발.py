import sys
sys.stdin = open('4613_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    
    min_count = N * M

    for w in range(1, N-1):
        w_count = 0
        for n in range(w):
            w_count += arr[n].count('W')

        for b in range(1, N-w):
            r = N - w - b
            count = N * M - w_count

            for n in range(w, w+b):
                count -= arr[n].count('B')

            for n in range(w+b, w+b+r):
                count -= arr[n].count('R')

            min_count = min(min_count, count)

    print('#{} {}'.format(t+1, min_count))