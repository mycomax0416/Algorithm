arr = [
[1, 2, 3, 4, 5],
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 23, 22, 21, 8],
[13, 12, 11, 10, 9]
]

min_x = 0
min_y = 0
max_x = len(arr[0]) - 1
max_y = len(arr) - 1
now_x = 0
now_y = 0

print((now_x, now_y), arr[now_y][now_x])

if now_x == min_x and now_y == min_y: #1
    while now_x < max_x:
        now_x += 1
        print((now_x, now_y), arr[now_y][now_x])

while arr[now_y][now_x] < 25:
    if now_x == max_x and now_y == min_y: #2
        min_y += 1
        while now_y < max_y:
            now_y += 1
            print((now_x, now_y), arr[now_y][now_x])

    if now_x == max_x and now_y == max_y: #3
        max_x -= 1
        while now_x > min_x:
            now_x -= 1
            print((now_x, now_y), arr[now_y][now_x])

    if now_x == min_x and now_y == max_y: #4
        max_y -= 1
        while now_y > min_y:
            now_y -= 1
            print((now_x, now_y), arr[now_y][now_x])

    if now_x == min_x and now_y == min_y: #1
        min_x += 1
        while now_x < max_x:
            now_x += 1
            print((now_x, now_y), arr[now_y][now_x])