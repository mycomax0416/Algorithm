import sys
sys.stdin = open('1979_sample_input.txt', 'r')

def find():
    global N

    for y in range(N):
        cal = 0

        for x in range(N):
            if arr[y][x] == 1:
                cal += 1

                if x == N-1:
                    dic[cal] += 1

            elif arr[y][x] == 0:
                dic[cal] += 1
                cal = 0

    for x in range(N):
        cal = 0

        for y in range(N):
            if arr[y][x] == 1:
                cal += 1
                
                if y == N-1:
                    dic[cal] += 1

            elif arr[y][x] == 0:
                dic[cal] += 1
                cal = 0
            


T = int(input())
for t in range(T):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dic = {}
    for l in range(N+1):
        dic[l] = 0

    find()

    print('#{} {}'.format(t+1, dic[K]))
