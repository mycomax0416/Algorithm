def input_code():
    global N, M

    for y in range(N):
        for x in range(M):
            if input_arr[y][x] == '1':
                start_points.append((x-3, y))
                start_points.append((x-2, y))
                start_points.append((x-1, y))
                start_points.append((x, y))
                break

        if input_arr[y][x] == '1':
            break

    return

def check_code(x, y):
    right = ''

    for idx in range(x+56, M):
        right += input_arr[y][idx]

    if '1' in right:
        start_points.remove((x, y))

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


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_arr = [input() for _ in range(N)]
    result = 0

    start_points = []
    input_code()


    for start_point in start_points:
        check_code(start_point[0], start_point[1])


    transed_codes = []

    for start_point in start_points:
        transed_code = []

        for group_idx in range(start_point[0], start_point[0]+56, 7):
            group = ''
            
            for idx in range(7):
                group += input_arr[start_point[1]][group_idx + idx]

            transed_code.append(trans_num(group))
                
        if None not in transed_code:
            transed_codes.append(transed_code)


    for test in transed_codes:
        key = 0
        odd = []
        even = []

        for idx in range(len(test)):
            if idx == len(test) - 1:
                key = test[idx]

            else:
                if idx % 2 == 0:
                    odd.append(test[idx])
                
                else:
                    even.append(test[idx])

        if (sum(odd)*3 + sum(even) + key) % 10 == 0:
            result = (sum(odd)+sum(even)+key)


    print('#{} {}'.format(t+1, result))
