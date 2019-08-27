# import sys
# sys.stdin = open('4875_sample_input.txt', 'r')

# T = int(input())

# for t in range(T):
#     N = int(input())

#     maze = []
#     for _ in range(N):
#         maze += [list(map(int, input()))]
#     # print(maze)  

#     visit = [[False] * (N) for _ in range(N)]
#     # print(visit)
#     result = 0

#     for y in range(N):
#         for x in range(N):
#             if maze[y][x] == 2:
#                 start_x, start_y = x, y

#             elif maze[y][x] == 3:
#                 finish_x, finish_y = x, y
#     # print(start_x, start_y)
#     # print(finish_x, finish_y)

#     stack = []
#     pre_x, pre_y = start_x, start_y 
#     stack += [[pre_x, pre_y]]
#     visit[pre_y][pre_x] = True
#     # print(stack)

#     while len(stack) > 0:
#         before_x, before_y = pre_x, pre_y

#         if pre_x == finish_x and pre_y == finish_y:
#             result = 1
#             break

#         elif maze[pre_y][pre_x+1] != 1 and visit[pre_y][pre_x+1] == False:  # 동
#             stack += [[pre_x+1, pre_y]]
#             visit[pre_y][pre_x+1] = True
#             pre_x += 1   

#         elif maze[pre_y][pre_x-1] != 1 and visit[pre_y][pre_x-1] == False:  # 서
#             stack += [[pre_x-1, pre_y]]
#             visit[pre_y][pre_x-1] = True
#             pre_x -= 1

#         elif maze[pre_y+1][pre_x] != 1 and visit[pre_y+1][pre_x] == False:  # 남
#             stack += [[pre_x, pre_y+1]]
#             visit[pre_y+1][pre_x] = True
#             pre_y += 1

#         elif maze[pre_y-1][pre_x] != 1 and visit[pre_y-1][pre_x] == False:  # 북
#             stack += [[pre_x, pre_y-1]]
#             visit[pre_y-1][pre_x] = True
#             pre_y -= 1

#         elif before_x == pre_x and before_y == pre_y:
#             before = stack.pop()
#             pre_x, pre_y = before[0], before[1]
        
#         print(pre_x, pre_y)
#         print(stack)
#     # print(visit)
#     print('----------')
#     # print(result)
#-----------------------------------------
import sys
sys.stdin = open('4875_sample_input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())

    maze = [[1 for _ in range(N+2)]]
    for _ in range(N):
        maze += [[1] + list(map(int, input())) + [1]]
    maze += [[1 for _ in range(N+2)]]

    visit = [[False] * (N+2) for _ in range(N+2)]
    result = 0

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 2:
                pre_x = x
                pre_y = y

            if maze[y][x] == 3:
                finish_x = x
                finish_y = y
    if finish_x == pre_x and finish_y == pre_y:
        result = 1

    stack = []
    stack += [[pre_x, pre_y]]

    while len(stack) > 0:
        if maze[pre_y][pre_x] == 3:
            result = 1
            break

        elif maze[pre_y][pre_x+1] != 1 and visit[pre_y][pre_x+1] == False:  # 동
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
            
    print('#{} {}'.format(t+1, result))
