import sys
sys.stdin = open('2001_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = []
    
    for n in range(N):
        arr.append(list(map(int, input().split())))
    
    test = []

    for y in range(N-M+1):
        for x in range(N-M+1):
            fly = []

            for dy in range(M):
                for dx in range(M):
                    fly.append(arr[y+dy][x+dx])

            test.append(sum(fly))

    print('#{} {}'.format(t+1, max(test)))
