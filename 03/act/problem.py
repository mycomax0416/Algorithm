arr = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]

result = []
min_x = 0
min_y = 0
max_x = len(arr[0])-1
max_y = len(arr)-1
count = 0
now_x = 0
now_y = 0

while count < 25:
    print(arr[now_y][now_x])

    if now_x == min_x and now_y == min_y:    
        while now_x < max_x:
            count += 1
            now_x += 1
            print(arr[now_y][now_x])
            print(now_x, now_y)
        min_y = min_y + 1
   
    elif now_x == max_x and now_y == min_y:
        while now_y < max_y:
            count += 1
            now_y += 1
            print(arr[now_y][now_x])
            print(now_x, now_y)
        min_x = min_x + 1
    
    elif now_x == max_x and now_y == max_y:
        while now_x >= min_x:
            count += 1
            now_x -= 1
            print(arr[now_y][now_x])
            print(now_x, now_y)
        min_y = min_y - 1
    
    else:
        while now_y >= max_y:
            count += 1
            now_y -= 1
            print(arr[now_y][now_x])
            print(now_x, now_y)
        min_x = min_x - 1