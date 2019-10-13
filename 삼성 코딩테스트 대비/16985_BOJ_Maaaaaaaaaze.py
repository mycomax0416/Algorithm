import sys, copy
from pprint import pprint
sys.stdin = open('16985_BOJ_input.txt', 'r')

 
empty = [[0]*5 for _ in range(5)]

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
def go():
    global min_count
    
    visit = [[[False]*5 for _ in range(5)] for _ in range(5)]
    Queue = [(0, 0, 0, 0)]
    visit[0][0][0] = True

    while Queue:
        test = Queue.pop(0)
        x, y, z = test[0], test[1], test[2]
        count = test[3]

        if x == 4 and y == 4 and z == 4:
            min_count = min(min_count, count)
            return

        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]

            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and visit[nz][ny][nx] == False and cube[nz][ny][nx] == 1:
                Queue.append((nx, ny, nz, count+1))
                visit[nz][ny][nx] = True


T = int(input())
for t in range(T):
    cube = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

    min_count = 125

    for _ in range(4):
        spin(0)
        if cube[0][0][0] == 1:
            print(_)

            for _ in range(4):
                spin(4)
                if cube[4][4][4] == 1:
                    print(_)


    if min_count == 125:
        min_count = -1

    print(min_count)