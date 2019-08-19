import sys
sys.stdin = open('1210_sample_input.txt', 'r')

for i in range(10):
    T = int(input())
    array = []

    for j in range(100):
        array += [[0] + list(map(int, input().split())) + [0]]

    y = 0
    answer = 0

    for x in range(101):
        if array[y][x] == 1:
            answer = x
            # print(x-1)

            while y < 99:
                if array[y][x-1] == 1:
                    while array[y][x-1] == 0:
                        x -= 1
                    y += 1

                elif array[y][x+1] == 1:
                    while array[y][x+1] == 0:
                        x += 1
                    y += 1

                else:
                    y += 1

        # print(array[99][x], end=' ')

        if array[y][x] == 2:
            print('#{} {}'.format(i + 1, answer-1))
            break
