import sys
sys.stdin = open('4861_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = []

    for j in range(N):
        arr += [input()]

    for y in range(N):
        for x in range(N-M+1):
            word = ''
            for lenth in range(M):
                word += arr[y][x+lenth]
          
            if word == word[::-1]:
                print('#{} {}'.format(i + 1, word))

    for x in range(N):
        for y in range(N-M+1):
            word = ''
            for lenth in range(M):
                word += arr[y+lenth][x]

            if word == word[::-1]:
                print('#{} {}'.format(i + 1, word))
