import sys
sys.stdin = open('input_1.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 5
    result_min_height = 5

    for y in range(N):
        test_y = []
        for t_x in range(N):
            test_y.append(arr[y][t_x])

        for x in range(N):
            test = test_y[:]
            test.remove(arr[y][x])
            for t_y in range(N):
                test.append(arr[t_y][x])

            heights = []
            for i in test:
                if i not in heights:
                    heights.append(i)

            for height in heights:
                cost = 0

                for j in test:
                    cost += abs(height-j)

                if cost < min_cost:
                    min_cost = cost
                    result_min_height = height

                elif cost == min_cost and height < result_min_height:
                    result_min_height = height


    print('#{} {} {}'.format(t+1, min_cost, result_min_height))