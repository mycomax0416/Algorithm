# import sys
# sys.stdin = open('17070_BOJ_input.txt')


def function(x_1, y_1, x_2, y_2):
    global count
    # print(x_1, y_1, x_2, y_2)

    if x_2 == N-1 and y_2 == N-1:
        count += 1
        return
    
    elif y_2 == y_1:
        if x_2+1 < N and arr[y_2][x_2+1] != 1 and x_2-x_1 == 1:
            function(x_1+1, y_1, x_2+1, y_2)    # 가로 - 가로
            if y_2+1 < N and arr[y_2+1][x_2+1] != 1 and arr[y_1+1][x_1+1] != 1:
                function(x_1+1, y_1, x_2+1, y_2+1)  # 가로 - 대각
        return
    elif x_2 == x_1:
        if y_2+1 < N and arr[y_2+1][x_1] != 1 and y_2-y_1 == 1:
            function(x_1, y_1+1, x_2, y_2+1)    # 세로 - 세로
            if x_2+1 < N and arr[y_2+1][x_2+1] != 1 and arr[y_1+1][x_1+1] != 1:
                function(x_1, y_1+1, x_2+1, y_2+1)    # 세로 - 대각
        return
    elif x_2-x_1 == 1 and y_2-y_1 == 1:
        if x_2+1 < N and arr[y_2][x_2+1] != 1:
            function(x_1+1, y_1+1, x_2+1, y_2)    # 대각 - 가로
            if y_2+1 < N and arr[y_2+1][x_2] != 1:
                function(x_1+1, y_1+1, x_2+1, y_2+1)  # 대각 - 대각
        
        if y_2+1 < N and arr[y_2+1][x_2] != 1:
            function(x_1+1, y_1+1, x_2, y_2+1)    # 대각 - 세로
        return


# T = int(input())
# for t in range(T):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
count = 0

function(0, 0, 1, 0)

print(count)