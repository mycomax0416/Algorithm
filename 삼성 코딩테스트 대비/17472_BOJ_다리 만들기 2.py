# import sys
# sys.stdin = open('17472_BOJ_input.txt', 'r')
from collections import deque
from pprint import pprint


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def island_numbering(input_x, input_y):
    queue = deque()
    queue.append((input_x, input_y))
    arr[input_y][input_x] = island_num
    visit = [[False]*M for _ in range(N)]
    visit[input_y][input_x] = True

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 1 and visit[ny][nx] == False:
                queue.append((nx, ny))
                arr[ny][nx] = island_num
                visit[ny][nx] = True

    
def connect_island(input_x, input_y, island_num):
    # x, y = input_x, input_y
    queue = deque()
    queue.append((input_x, input_y))
    visit = [[False]*M for _ in range(N)]
    visit[input_y][input_x] = True

    while queue:
        x, y = queue.popleft()
        # print(x, y)

        mx_1 = x-1
        # print(mx_1)
        if 0 < mx_1 and arr[y][mx_1] == 0:
            while arr[y][mx_1] == 0 and mx_1 > 0:
                mx_1 -= 1
            if arr[y][mx_1] != 0 and arr[y][mx_1] != island_num:
                if x-mx_1-1 > 1 and (arr[y][mx_1], x-mx_1-1) not in G[island_num]:
                    G[island_num].append((arr[y][mx_1], x-mx_1-1)) 
                    G[arr[y][mx_1]].append((island_num, x-mx_1-1))
        mx_2 = x+1
        if mx_2 < M-2 and arr[y][mx_2] == 0:
            # print(mx_2)
            while arr[y][mx_2] == 0 and mx_2 < M-1:
                mx_2 += 1
            if arr[y][mx_2] != 0 and arr[y][mx_2] != island_num:
                if mx_2-x-1 > 1 and (arr[y][mx_2], mx_2-x-1) not in G[island_num]:
                    G[island_num].append((arr[y][mx_2], mx_2-x-1))
                    G[arr[y][mx_2]].append((island_num, mx_2-x-1))
        my_1 = y-1
        if 0 < my_1 and arr[my_1][x] == 0:
            while arr[my_1][x] == 0 and my_1 > 0:
                my_1 -= 1
            if arr[my_1][x] != 0 and arr[my_1][x] != island_num:
                if y-my_1-1 > 1 and (arr[my_1][x], y-my_1-1) not in G[island_num]:
                    G[island_num].append((arr[my_1][x], y-my_1-1))
                    G[arr[my_1][x]].append((island_num, y-my_1-1))
        my_2 = y+1
        if my_2 < N-1 and arr[my_2][x] == 0:
            while arr[my_2][x] == 0 and my_2 < N-1:
                my_2 += 1
            if arr[my_2][x] != 0 and arr[my_2][x] != island_num:
                if my_2-y-1 > 1 and (arr[my_2][x], my_2-y-1) not in G[island_num]:
                    G[island_num].append((arr[my_2][x], my_2-y-1))
                    G[arr[my_2][x]].append((island_num, my_2-y-1))


        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == island_num and visit[ny][nx] == False:
                queue.append((nx, ny))
                visit[ny][nx] = True


# T = int(input())
# for t in range(T):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

islands = []
island_num = 1
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            island_num += 1
            island_numbering(x, y)
            islands.append((x, y, island_num))

G = [[] for _ in range(island_num+1)]
# pprint(arr)

for island in islands:
    x, y, num = island
    connect_island(x, y, num)
# print(G)

# print(len(islands))
key = [10 for _ in range(island_num+1)]
key[0], key[1], key[2] = 0, 0, 0
# print(key)

# print(len(islands), island_num+1)
count = len(islands)
visit = [False for _ in range(island_num+1)]
visit[0], visit[1] = True, True
result = 0
# print(count)

while count:
    min_len = 10
    for idx in range(2, island_num+1):
        if not  visit[idx] and min_len > key[idx]:
            u, min_len = idx, key[idx]

    visit[u] = True
    result += key[u]
    # print(u, key[u])

    for v, w in G[u]:
        if not visit[v] and w < key[v]:
            key[v] = w

    count -= 1

if result == 0:
    result = -1

print(result)