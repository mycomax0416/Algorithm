import sys
sys.stdin = open('4875_sample_input.txt', 'r')

T = int(input())

for t in range(1):
    N = int(input())

    maze = [[1 for _ in range(N+2)]]
    for _ in range(N):
        maze += [[1] + list(map(int, input())) + [1]]
    maze += [[1 for _ in range(N+2)]]

    visit = [[False] * (N+2) for _ in range(N+2)]
    result = 0
    # print(maze)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 2:
                pre_x = x
                pre_y = y

            if maze[y][x] == 3:
                finish_x = x
                finish_y = y

    stack = []
    stack += [[pre_x, pre_y]]
    print(stack)

    while len(stack) > 0:
        # if maze[pre_y][pre_x] == 3 and visit[pre_y][pre_x] == True:
        #     result = 1
        #     break
        # if pre_x == finish_x and pre_y == finish_y:
        #     result = 1
        #     break

        if maze[pre_y][pre_x+1] != 1 and visit[pre_y][pre_x+1] == False:  # 동
            stack += [[pre_x+1, pre_y]]
            visit[pre_y][pre_x+1] = True
            pre_x += 1

        elif maze[pre_y][pre_x-1] != 1 and visit[pre_y][pre_x-1] == False:  # 서
            stack += [[pre_x-1, pre_y]]
            visit[pre_y][pre_x-1] = True
            pre_x -= 1

        elif maze[pre_y+1][pre_x] != 1 and visit[pre_y+1][pre_x] == False:  # 남
            stack += [[pre_x, pre_y+1]]
            visit[pre_y+1][pre_x] = True
            pre_y += 1

        elif maze[pre_y-1][pre_x] != 1 and visit[pre_y-1][pre_x] == False:  # 북
            stack += [[pre_x, pre_y-1]]
            visit[pre_y-1][pre_x] = True
            pre_y -= 1

        else:
            before = stack.pop()
            pre_x, pre_y = before[0], before[1]
    
        print(stack)

    if visit[finish_y][finish_x] == True:
        result = 1
            
    # print('#{} {}'.format(t+1, result))
    # print(visit)
