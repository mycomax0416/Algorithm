import sys
sys.stdin = open('5188_sample_input.txt', 'r')

#   오른쪽, 아래
dx = [1, 0]
dy = [0, 1]

def collect(x, y, path_sum):
    global min_sum

    if x == N-1 and y == N-1:
        min_sum = min(min_sum, path_sum)
        return

    else:
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx <= N-1 and ny <= N-1:
                collect(nx, ny, path_sum + arr[ny][nx])


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 10 * N * 2

    collect(0, 0, arr[0][0])

    print('#{} {}'.format(t+1, min_sum))