import sys
sys.stdin = open('암호코드 스캔_sample_input.txt', 'r')


def input_code():
    global N, M

    for y in range(N):
        start_x = 0
        group = ''

        for x in range(M):
            if input_arr[y][x] != '0':
                group += input_arr[y][x]
        
        print(group)
    return


T = int(input())
for t in range(1):
    N, M = map(int, input().split())
    input_arr = [input() for _ in range(N)]

    test_group = []
    # print(input_arr)

    # print(int('68B46DDB9346F4000', 16))
    input_code()
    print(test_group)
