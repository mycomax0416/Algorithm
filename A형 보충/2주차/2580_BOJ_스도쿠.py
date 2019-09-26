import sys
sys.stdin = open('2580_BOJ_input.txt', 'r')


def sudoku():
    global flag

    if flag == True:            # 중복정답 제거
        return

    test_x, test_y = 10, 10

    for y in range(9):                              # 빈칸 찾기
        for x in range(9):
            if arr[y][x] == 0:
                test_x, test_y = x, y
                break
        if test_x != 10:
            break

    if test_x == 10:                                # 정답
        for result in arr:
            print(' '.join(map(str, result)))
        flag = True
        return

    subs = [n for n in range(1, 10)]                # 후보군

    for n in range(9):                              # 가로, 세로
        if arr[n][test_x] in subs:
            subs.remove(arr[n][test_x])

        if arr[test_y][n] in subs:
            subs.remove(arr[test_y][n])

    if test_x < 3:                              # 사각형
        left_x, right_x = 0, 3
    elif 3 <= test_x < 6:
        left_x, right_x = 3, 6
    else:
        left_x, right_x = 6, 9

    if test_y < 3:
        top_y, bottom_y = 0, 3
    elif 3 <= test_y < 6:
        top_y, bottom_y = 3, 6
    else:
        top_y, bottom_y = 6, 9

    for y in range(top_y, bottom_y):
        for x in range(left_x, right_x):
            if arr[y][x] in subs:
                subs.remove(arr[y][x])

    if not subs:                                    # 오답
        return

    for sub in subs:
        arr[test_y][test_x] = sub

        sudoku()

        arr[test_y][test_x] = 0
    return


arr = [list(map(int, input().split())) for _ in range(9)]

flag = False

sudoku()