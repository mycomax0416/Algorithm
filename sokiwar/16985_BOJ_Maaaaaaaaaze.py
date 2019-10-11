import sys, copy
from pprint import pprint
# sys.stdin = open('16985_BOJ_input.txt', 'r')

 
empty = [[0]*5 for _ in range(5)]
# print(empty)
# visit = [[[False]*5 for _ in range(5)] for _ in range(5)]
# print(visit)

def spin(k):
    clone = copy.deepcopy(empty)

    for y in range(5):
        for x in range(4, -1, -1):
            clone[4-y][x] = cube[k][x][y]

    cube[k] = clone


# 동 서 남 북 아래 위
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
def go(x, y, z):
    global min_count

    # if count >= min_count:
    #     return

    # elif x == 4 and y == 4 and z == 4:
    #     min_count = min(min_count, count)
    
    visit = [[[False]*5 for _ in range(5)] for _ in range(5)]
    Queue = [(1, 1, 1)]
    visit[1][1][1] = True
    count = 0

    while Queue:
        count += 1
        test = Queue.pop(0)
        x, y, z = test[0], test[1], test[2]

        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]

            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and visit[nz][ny][nx] == False and cube[nz][ny][nx] == 1:
                Queue.append(nx, ny, nz)
                visit[nz][ny][nx] = True


# T = int(input())
# for t in range(T):
cube = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
# pprint(cube[0])

min_count = 125

for _ in range(4):
    spin(0)
    if cube[0][0][0] == 1:

        for _ in range(4):
            spin(4)
            if cube[4][4][4] == 1:

                for _ in range(4):
                    spin(1)

                    for _ in range(4):
                        spin(2)

                        for _ in range(4):
                            spin(3)

                            # go(0, 0, 0, 0)
            

if min_count == 125:
    print(-1)
else:
    print(min_count)