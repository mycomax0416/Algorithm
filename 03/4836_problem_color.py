import sys
sys.stdin = open('4836_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N = int(input())

    arr = [[0] * 10 for _ in range(10)]
    result = 0

    for j in range(N):
        get_color_info = list(map(int, input().split()))

        for n in range(get_color_info[1]-1, get_color_info[3]):
            for m in range(get_color_info[0]-1, get_color_info[2]):
                arr[n][m] += get_color_info[4]

    for y in range(10):
        for x in range(10):
            if arr[y][x] > 2:
                result += 1
            
    print('#{} {}'.format(i + 1, result))