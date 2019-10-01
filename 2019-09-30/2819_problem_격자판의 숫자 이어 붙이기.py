import sys
sys.stdin = open('2819_sample_input.txt', 'r')

#   동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def backtrack(x, y, k, n):
    if k >= 6:
        case.add(n)
        # if n not in case:
        #     case.append(n)
        return

    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 4 and 0 <= ny < 4:
                backtrack(nx, ny, k+1, n*10+arr[ny][nx])


T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]

    # case = []
    case = set()

    for y in range(4):
        for x in range(4):
            backtrack(x, y, 0, arr[y][x])

    print('#{} {}'.format(t+1, len(case)))