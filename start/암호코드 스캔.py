import sys, copy
sys.stdin = open('암호코드 스캔_sample_input.txt', 'r')


def find_code():
    global N, M
    left_x, right_x = 0, 0
    top_y = 0
    bottom_y = 0

    for y in range(N):
        for x in range(M):
            if input_arr[y][x] != '0':
                left_x = x
                top_y = y
                break

        if input_arr[y][x] != '0':
                break

    for y in range(top_y, N):
        if input_arr[y][left_x] == '0':
            bottom_y = y - 1
            break


    on = True
    while on:
        if right_x+1 >= M:
            on = False
        
        else:
            right_x += 1

            for y in range(top_y, bottom_y):
                if input_arr[y][right_x] != input_arr[y+1][right_x]:
                    on = False
                    break

    #---------------------------
    code_16 = list(input_arr[top_y][left_x:right_x])


    while code_16[-1] == '0':
        code_16.pop()
        right_x -= 1

    # for _ in range(len(code_16)):
    #     if code_16[-1] == '0':
    #         code_16.pop()
    #         right_x -= 1
    #     else:
    #         break

    codes_16.append(''.join(code_16))
    #---------------------------------

    for y in range(top_y, bottom_y+1):
        for x in range(left_x, right_x+1):
            input_arr[y][x] = '0'

    return


def trans_num(code):
    if code == '0001101':
        return 0

    elif code == '0011001':
        return 1

    elif code == '0010011':
        return 2

    elif code == '0111101':
        return 3

    elif code == '0100011':
        return 4

    elif code == '0110001':
        return 5

    elif code == '0101111':
        return 6

    elif code == '0111011':
        return 7

    elif code == '0110111':
        return 8

    elif code == '0001011':
        return 9

    return


def interpret_code(code_16):
    global result

    code_10 = int(code_16, 16)
    code_2 = list(bin(code_10)[2:])

    while code_2[-1] == '0':
        code_2.pop()

    q, r = divmod(len(''.join(code_2)), 56)

    while r != 56:
        r += 1
        code_2.insert(0, '0')
    

    short_code = []
    overlap = len(code_2) // 56
    for idx in range(0, len(code_2), overlap):
        short_code.append(code_2[idx])


    num_code = []
    for point in range(0, len(short_code), 7):
        group = []

        for idx in range(7):
            group.append(short_code[point+idx])

        num_code.append(trans_num(''.join(group)))

    key = 0
    odd = []
    even = []
    for idx in range(len(num_code)):
        if idx == 7:
            key = num_code[idx]

        elif idx % 2 == 0:
            odd.append(num_code[idx])
        
        else:
            even.append(num_code[idx])

    if (sum(odd)*3 + sum(even) + key) % 10 == 0:
        result += (sum(odd)+sum(even)+key)
   
    return


T = int(input())
for t in range(12):
    N, M = map(int, input().split())
    input_arr = [list(input()) for _ in range(N)]
    result = 0


    codes_16 = []
    while input_arr != [['0'] * M for _ in range(N)]:
        find_code()
    print(codes_16)


    # for code_16 in codes_16:
    #     interpret_code(code_16)


    # print('#{} {}'.format(t+1, result))
    # print('==========')
