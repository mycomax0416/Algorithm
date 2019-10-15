import sys
sys.stdin = open('5250_sample_input.txt', 'r')

#   동 남
dx = [1, 0]
dy = [0, 1]
def function(x, y, cost):
    global min_cost

    if x == N-1 and y == N-1:
        min_cost = min(min_cost, cost)
        return

    else:
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < N and ny < N:
                if arr[ny][nx] <= arr[y][x]:
                    function(nx, ny, cost+1)
                else:
                    function(nx, ny, cost+1+arr[ny][nx]-arr[y][x])


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    DP = [0xfffff*N for _ in range(N)]
    min_cost = 0xfffff

    function(0, 0, 0)

    print('#{} {}'.format(t+1, min_cost))