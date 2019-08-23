T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]
    result = 0
    
    for _ in range(M):
        xy = list(map(int, input().split()))
        x1, y1 = xy[0], xy[1]
        x2, y2 = xy[2], xy[3]
        for y in range(y1-1, y2):
            for x in range(x1-1, x2):
                arr[y][x] = 1
    
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                result += 1

    print('#{} {}'.format(tc+1, result))