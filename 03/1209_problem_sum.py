import sys
sys.stdin = open('1209_sample_input.txt', 'r')

for i in range(10):
    T = input()
    arr = []
    for j in range(100):
        arr_y = list(map(int, input().split()))
        arr += [arr_y]
 
    result = []
   
    for y in range(100):
        result += [sum(arr[y])]

    for x in range(100):
        sum_y = []
        for y in range(100):
            sum_y += [arr[y][x]]
        result += [sum(sum_y)]

    for x in range(100):
        sum_cross_1 = []
        sum_cross_1 += [arr[x][x]]
        result += [sum(sum_cross_1)]

    for x in range(100, -1):
        sum_cross_2 = []
        sum_cross_2 += [arr[y][x]]
        result += [sum(sum_cross_2)]
            
    print('#{} {}'.format(i + 1, max(result)))