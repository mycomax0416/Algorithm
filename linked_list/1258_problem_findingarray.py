import sys
sys.stdin = open('1258_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    empty = [[0] * N for _ in range(N)]
    arr = []
    size = []
    result = ''

    for n in range(N):
        arr.append(list(map(int, input().split())))

    while arr != empty:
        row, column = 1, 1
        
        for y in range(N):
            for x in range(N):
                if arr[y][x] != 0:
                    start_x, start_y = x, y
                    break
        
            if arr[y][x] != 0:
                break

        while arr[start_y][start_x+row] != 0:
            row += 1

        while arr[start_y+column][start_x] != 0:
            column += 1

        for y in range(start_y, start_y + column):
            for x in range(start_x, start_x + row):
                arr[y][x] = 0
        
        size.append([column, row])
        
    result += str(len(size))

    while size:
        out = size.pop(0)
    
        for _ in range(len(size)):
            test = size.pop(0)
            if out[0]*out[1] > test[0]*test[1]:
                out, test = test, out

            elif out[0]*out[1] == test[0]*test[1]:
                if out[0] > test[0]:
                    out, test = test, out

            size.append(test)
        
        for n in out:
            result += ' ' + str(n)
   
    print('#{} {}'.format(t+1, result))
