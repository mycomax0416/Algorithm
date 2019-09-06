import sys
sys.stdin = open('1974_sample_input.txt', 'r')


def test_row():
    sign = True

    for y in range(9):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for x in range(9):
            if arr[y][x] in num:            
                num.remove(arr[y][x])
                
            else:
                sign = False
                return sign

    return sign


def test_column():
    sign = True

    for x in range(9):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for y in range(9):
            if arr[y][x] in num:            
                num.remove(arr[y][x])

            else:
                sign = False
                return sign

    return sign


def test_box():
    sign = True

    for point_x in range(0, 7, 3):
        for point_y in range(0, 7, 3):
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            for y in range(point_y, point_y + 3, 1):
                for x in range(point_x, point_x + 3, 1):
                    if arr[y][x] in num:            
                        num.remove(arr[y][x])
                
                    else:
                        sign = False
                        return sign
            
    return sign


T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if False in [test_row(), test_column(), test_box()]:
        result = 0
    
    else:
        result = 1

    print('#{} {}'.format(t+1, result))
