# import sys
# sys.stdin = open('14890_BOJ_input.txt', 'r')


def check_column(x, value):
    global count

    if x == N-1:
        if arr[y][x] == value:
            count += 1
        return

    elif value == arr[y][x+1]:
        check_column(x+1, value)

    elif L-1 <= x and value+1 == arr[y][x+1]:
        flag = True

        for l in range(L):
            if visit[x-l] == False:
                visit[x-l] = True
            else:
                flag = False

        if flag:
            check_column(x+1, value+1)

    elif x < N-L and value-1 == arr[y][x+1]:
        flag = True

        for l in range(L):
            if value-1 == arr[y][x+1+l]:
                visit[x+1+l] = True
            else:
                flag = False

        if flag:
            check_column(x+L, value-1)


def check_row(y, value):
    global count

    if y == N-1:
        if arr[y][x] == value:
            count += 1
        return

    elif value == arr[y+1][x]:
        check_row(y+1, value)

    elif L-1 <= y and value+1 == arr[y+1][x]:
        flag = True

        for l in range(L):
            if visit[y-l] == False:
                visit[y-l] = True
            else:
                flag = False

        if flag:
            check_row(y+1, value+1)

    elif y < N-L and value-1 == arr[y+1][x]:
        flag = True

        for l in range(L):
            if value-1 == arr[y+1+l][x]:
                visit[y+1+l] = True
            else:
                flag = False
        
        if flag:
            check_row(y+L, value-1)


# T = int(input())
# for t in range(T):
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

count = 0

for y in range(N):
    visit = [False for _ in range(N)]
    check_column(0, arr[y][0])

for x in range(N):
    visit = [False for _ in range(N)]
    check_row(0, arr[0][x])

print(count)