import sys
sys.stdin = open('2667_BOJ_input.txt', 'r')


def find():
    global count

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                count += 1
                return x, y


#   동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(start_x, start_y):
    stack = []

    stack.append((start_x, start_y))
    size = 1
    visit[start_y][start_x] = True
    arr[start_y][start_x] = 0

    while stack:
        x, y = stack[-1][0], stack[-1][1]
        pre_x, pre_y = x, y

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False and arr[ny][nx] == 1:
                stack.append((nx, ny))
                size += 1
                visit[ny][nx] = True
                arr[ny][nx] = 0
                x, y = nx, ny
                break

        if pre_x == x and pre_y == y:
            stack.pop()

    return size


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
empty = [[0] * N for _ in range(N)]

count = 0
sizes = []

while arr != empty:
    x, y = find()
    sizes.append(DFS(x, y))

print(count)

sizes.sort()

for size in sizes:
    print(size)
