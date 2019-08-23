T = int(input())

for tc in range(T):
    N = int(input())

    arr = []
    empty_arr = [[0] * N for _ in range(N)]

    for _ in range(N):
        arr += [list(map(int, input().split()))]

        result = 0

    while arr == empty_arr:
        
        pre_x, pre_y = 0, 0 # 처음 x, y 찾기

        for y in range(N):
            for x in range(N):
                if arr[y][x] != 0:
                    pre_x, pre_y = x, y
                    break

            if arr[y][x] != 0:
                    pre_x, pre_y = x, y
                    break

        # glo_l_x, glo_r_x = pre_x, pre_x     # 섬 넓이 좌표
        # glo_t_y, glo_b_y = pre_y, pre_y
        #-------------------------------------
        
        l_x, r_x = pre_x, pre_x     # 이동 로직
        t_y, b_y = pre_y, pre_y

        if arr[t_y][l_x-1] != 0:    # 왼 위 -> 왼
            while arr[t_y][l_x-1] != 0:
                l_x -= 1


        if arr[t_y-1][l_x] != 0:    # 왼 위 -> 위
            while arr[t_y-1][l_x] != 0:
                t_y -= 1
        

        if arr[t_y][r_x+1] != 0:    # 오 위 -> 오
            while arr[t_y][r_x+1] != 0:
                r_x += 1


        if arr[t_y-1][r_x] != 0:    # 오 위 -> 위
            while arr[t_y-1][r_x] != 0:
                t_y -= 1


        if arr[b_y][l_x-1] != 0:    # 왼 밑 -> 왼
            while arr[b_y][l_x-1] !=0:
                l_x -= 1


        if arr[b_y+1][l_x] != 0:    # 왼 밑 -> 밑
            while arr[b_y+1][l_x] != 0:
                b_y += 1


        if arr[b_y][r_x+1] != 0:    # 오 밑 -> 오
            while arr[b_y][r_x+1] != 0:
                r_x += 1


        if arr[b_y+1][r_x] != 0:    # 오 밑 -> 밑
            while arr[b_y+1][r_x] != 0:
                b_y += 1
        

        if arr[t_y-1][l_x-1] != 0:  # 왼 위 -> 대각선
            while arr[t_y-1][l_x-1] != 0:
                t_y -= 1
                l_x -= 1


        if arr[t_y-1][r_x+1] != 0:  # 오 위 -> 대각선
            while arr[t_y-1][r_x+1] != 0:
                t_y -= 1
                r_x += 1


        if arr[b_y+1][l_x-1] != 0:  # 아래 윈 -> 대각선
            while arr[b_y+1][l_x-1] != 0:
                b_y += 1
                l_x -= 1

        
        if arr[b_y+1][r_x+1] != 0:  # 아래 오 -> 대각선
            while arr[b_y+1][r_x+1] != 0:
                b_y += 1
                r_x += 1


        print(l_x, r_x)
        print(t_y, b_y)
        # for y in range(t_y, b_y+1):
        #     for x in range(l_x, r_x+1):
        #         arr[y][x] = 0
        # print(arr)

        # result += 1
    # print(arr)
    # print(result)




    