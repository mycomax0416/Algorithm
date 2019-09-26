import sys
sys.stdin = open('input_2.txt', 'r')


def find():
    for y in range(10):
        for x in range(10):
            if arr[y][x] == 9:
                return x, y


def cookie(k, distance):
    global min_distance

    if k >= 6:
        min_distance = min(min_distance, distance)
        return

    if distance > min_distance:
        return

    else:
        start_x, start_y = find()
        befo_x, befo_y = start_x, start_y

        for y in range(10):
            for x in range(10):
                if arr[y][x] != 0 and arr[y][x] != 9:
                    befo_cookie = arr[y][x]
                    arr[start_y][start_x] = 0
                    arr[y][x] = 0

                    cookie(k+1, distance+(abs(start_x-x)+abs(start_y-y)))

                    arr[start_y][start_x] = 9
                    arr[y][x] = befo_cookie


T = int(input())
for t in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(10)]

    min_distance = 20 * 6

    cookie(0, 0)

    print('#{} {}'.format(t+1, min_distance))