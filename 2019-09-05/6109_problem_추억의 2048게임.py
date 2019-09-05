import sys
sys.stdin = open('6109_sample_input.txt', 'r')

def up():
    global N
    global arr
    arr_yx = [[] for _ in range(N)]
    
    for x in range(N):
        column = []

        for y in range(N):
            column.append(arr[y][x])                

        for first in range(N):
            for second in range(first+1, N):
                if column[first] == column[second]:
                    column[first] *= 2
                    column[second] = 0
                    break

                elif column[first] != column[second] and column[second] != 0:
                    break
        
        for idx in range(N-1, -1, -1):
            if column[idx] == 0:
                column.append(column.pop(idx))
        
        for chr in column:
            arr_yx[x].append(chr)

    arr_xy = [[''] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            arr_xy[y][x] = arr_yx[x][y]

    arr = arr_xy
    return arr


def down():
    global N
    global arr
    arr_yx = [[] for _ in range(N)]

    for x in range(N):
        column = []

        for y in range(N):
            column.append(arr[y][x])

        for first in range(N-1, -1, -1):
            for second in range(first-1, -1, -1):
                if column[first] == column[second]:
                    column[first] *= 2
                    column[second] = 0
                    break

                elif column[first] != column[second] and column[second] != 0:
                    break


        for idx in range(N):
            if column[idx] == 0:
                column.insert(0, column.pop(idx))

        for chr in column:
            arr_yx[x].append(chr)

    arr_xy = [[''] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            arr_xy[y][x] = arr_yx[x][y]

    arr = arr_xy
    return arr


def left():
    global N
    global arr
    arr_xy = [[] for _ in range(N)]

    for y in range(N):
        row = arr[y]

        for first in range(N):
            for second in range(first+1, N):
                if row[first] == row[second]:
                    row[first] *= 2
                    row[second] = 0
                    break

                elif row[first] != row[second] and row[second] != 0:
                    break

        for idx in range(N-1, -1, -1):
            if row[idx] == 0:
                row.append(row.pop(idx))

        for chr in row:
            arr_xy[y].append(chr)

    arr = arr_xy
    return


def right():
    global N
    global arr
    arr_xy = [[] for _ in range(N)]

    for y in range(N):
        row = arr[y]

        for first in range(N-1, -1, -1):
            for second in range(first-1, -1, -1):
                if row[first] == row[second]:
                    row[first] *= 2
                    row[second] = 0
                    break

                elif row[first] != row[second] and row[second] != 0:
                    break
        
        for idx in range(N):
            if row[idx] == 0:
                row.insert(0, row.pop(idx))

        for chr in row:
            arr_xy[y].append(chr)

    arr = arr_xy
    return


T = int(input())
for t in range(T):
    N, S = input().split()
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    print('#{}'.format(t+1))

    if S == 'up':
        up()

    elif S == 'down':
        down()

    elif S == 'right':
        right()

    elif S == 'left':
        left()

    
    for n in range(N):
        arr[n] = list(map(str, arr[n]))
        print(' '.join(arr[n]))
