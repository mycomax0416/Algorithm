import copy#, sys
# sys.stdin = open('17143_BOJ_input.txt', 'r')


def catch(x):
    global size_sum

    for y in range(R):
        if arr[y][x] != 0:
            size_sum += arr[y][x][2]
            arr[y][x] = 0
            return


def move(x, y, s, d, z, k):
    if k == 0:
        if after_arr[y][x] != 0:
            if after_arr[y][x][0] > s:
                return

        else:
            after_arr[y][x] = (s, d, z)


    else:
        if d == 1 and 0 <= y < R:   # 위
            if y == 0:
                move(x, y+1, s, 2, z, k-1)
            else:
                move(x, y-1, s, 1, z, k-1)

        elif d == 2 and 0 <= y < R: # 아래
            if y == R-1:
                move(x, y-1, s, 1, z, k-1)
            else:
                move(x, y+1, s, 2, z, k-1)

        elif d == 3 and 0 <= x < C: # 오른쪽
            if x == C-1:
                move(x-1, y, s, 4, z, k-1)
            else:
                move(x+1, y, s, 3, z, k-1)

        elif d == 4 and 0 <= x < C: # 왼쪽
            if x == 0:
                move(x+1, y, s, 3, z, k-1)
            else:
                move(x-1, y, s, 4, z, k-1)


# T = int(input())
# for t in range(T):
R, C, M = map(int, input().split())

arr = [[0]*(C) for _ in range(R)]
empty_arr = copy.deepcopy(arr)

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = (s, d, z)

size_sum = 0

for idx in range(C):
    catch(idx)
    after_arr = copy.deepcopy(empty_arr)

    for y in range(R):
        for x in range(C):
            if arr[y][x] != 0:
                s, d, z = arr[y][x]
                move(x, y, s, d, z, s)
    
    arr = after_arr[:]

print(size_sum)