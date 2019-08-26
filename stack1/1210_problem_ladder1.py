import sys
sys.stdin = open('1210_sample_input.txt', 'r')

for i in range(10):
    T = int(input())
    array = []

    for j in range(100):
        array += [[0] + list(map(int, input().split())) + [0]]

    for test_x in range(101):
        x = test_x
        y = 0

        if array[y][x] == 1:
            while y < 99:
                y += 1

                if array[y][x-1] == 1:
                    while array[y][x-1] == 1:
                        x -= 1

                elif array[y][x+1] == 1:
                    while array[y][x+1] == 1:
                        x += 1

        if array[y][x] == 2:
            print('#{} {}'.format(i + 1, test_x-1))
            break
