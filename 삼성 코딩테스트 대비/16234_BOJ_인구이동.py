# import sys
from collections import deque
# sys.stdin = open('16234_BOJ_input.txt', 'r')


def find():
    for y in range(N):
        for x in range(N):
            if visit[y][x] == False:
                return x, y

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def function(input_x, input_y):
    Queue = deque()
    Queue.append((input_x, input_y))
    visit[input_y][input_x] = True
    group = deque()
    group.append((input_x, input_y))
    sum_group = arr[input_y][input_x]

    while Queue:
        x, y = Queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False and L <= abs(arr[y][x]-arr[ny][nx]) <= R:
                Queue.append((nx, ny))
                group.append((nx, ny))
                sum_group += arr[ny][nx]
                visit[ny][nx] = True
    
    average = sum_group // len(group)
    
    for x, y in group:
        arr[y][x] = average


# T = int(input())
# for t in range(T):
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

finish = [[True]*N for _ in range(N)]
move = -1
count = 0

while count != N*N:
    count = 0
    visit = [[False]*N for _ in range(N)]

    while visit != finish:
        x, y = find()
        count += 1
        function(x, y)

    move += 1

print(move)

# 정답 ---------------------------------------
# def BFS(x, y):
#     global N, L, R
#     f = r = -1                          # f = front, r = rear
#     visit[x][y] = True; S = MAP[x][y]
#     r += 1
#     Q[r][0], Q[r][1] = x, y
#     while f != r:
#         f += 1
#         x, y = Q[f][0], Q[f][1]
#         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             tx, ty = x + dx, y + dy
#             if 0 <= tx < N and 0 <= ty < N and not visit[tx][ty]:
#                 if L <= abs(MAP[tx][ty] - MAP[x][y]) <= R:
#                     visit[tx][ty] = True; S += MAP[tx][ty]
#                     r += 1
#                     Q[r][0], Q[r][1] = tx, ty
#     if r > 0:
#         S = S // (r + 1)
#         for i in range(0, r + 1):
#             MAP[Q[i][0]][Q[i][1]] = S
#         return True
#     else:
#         return False
# # -----------------------------------------------

# N, L, R = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# Q = [[0, 0] for _ in range(N * N)]

# cnt = 0
# while True:
#     flag = False
#     visit = [[False] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if not visit[i][j]:
#                 flag |= BFS(i, j)

#     if not flag: break
#     cnt += 1
# print(cnt)