import sys
sys.stdin = open('1861_sample_input.txt', 'r')

#   동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
 
def go(input_x, input_y):
    global max_count
 
    x, y = input_x, input_y
    stack = []
    stack.append((input_x, input_y))
 
    count = 1
    while stack:
        print(stack)
        x, y = stack.pop(0)
 
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
 
            if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == arr[y][x]+1:
                stack.append((nx, ny))
                count += 1
 
    return count
 
 
T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    max_count = 0
    min_value = N**2
 
    for y in range(N):
        for x in range(N):
            count = go(x, y)
 
            if max_count == count:
                min_value = min(min_value, arr[y][x])
             
            elif count > max_count:
                max_count = count
                min_value = arr[y][x]
 
    print('#{} {} {}'.format(t+1, min_value, max_count))