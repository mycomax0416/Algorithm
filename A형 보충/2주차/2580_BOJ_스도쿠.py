import sys
sys.stdin = open('2580_BOJ_input.txt', 'r')


def check():
    for y in range(9):
        for x in range(9):
            if arr[y][x] == 0:
                return x, y

    return True


def sudoku(input_x, input_y):
    # if check():
    #     print(arr)

    # else:
    sub = [n for n in range(1, 10)]
    for n in range(9):
        if arr[n][input_x] in sub:      # 세로
            sub.remove(arr[n][input_x])

        if arr[input_y][n] in sub:      # 가로
            sub.remove(arr[input_y][n])

        if x < 3:
            pass


    print(sub)
    return

arr = [list(map(int, input().split())) for _ in range(9)]
sudoku(4, 1)
