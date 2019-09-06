import sys, copy
from collections import deque
sys.stdin = open('15683_BOJ_input.txt', 'r')


#       동 서 남 북
dx_1 = [[1], [-1], [0], [0]]
dy_1 = [[0], [0], [1], [-1]]

#       동 서      남 북
dx_2 = [[1, -1], [0, 0]]
dy_2 = [[0, 0], [1, -1]]

#       북 동   동 남       남 서   서 북
dx_3 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dy_3 = [[-1, 0], [0, 1], [1, 0], [0, -1]]

#       동 서 남    동 서 북        동 남 북    서 남 북
dx_4 = [[1, -1, 0], [1, -1, 0], [1, 0, 0], [-1, 0, 0]]
dy_4 = [[0, 0, 1], [0, 0, -1], [0, 1, -1], [0, 1, -1]]

#   동 서 남 북
dx_5 = [[1, -1, 0, 0]]
dy_5 = [[0, 0, 1, -1]]


def cctv_1(x, y, d):    # 1번 cctv 일때의 주어진 방향(dx_1)에 대해서 0인 arr를 #으로 바꾸는 함수
    global N, M         # 밑에 카메라 함수들 또한 동일

    for idx in range(1):  
        nx = x + dx_1[d][idx]
        ny = y + dy_1[d][idx]

        while 0 <= nx < M and 0 <= ny < N and test_arr[ny][nx] != 6:
            if test_arr[ny][nx] in camera:
                nx += dx_1[d][idx]
                ny += dy_1[d][idx]

            else:
                test_arr[ny][nx] = '#'
                nx += dx_1[d][idx]
                ny += dy_1[d][idx]

    return


def cctv_2(x, y, d):
    global N, M

    for idx in range(2):  
        nx = x + dx_2[d][idx]
        ny = y + dy_2[d][idx]

        while 0 <= nx < M and 0 <= ny < N and test_arr[ny][nx] != 6:
            if test_arr[ny][nx] in camera:
                nx += dx_2[d][idx]
                ny += dy_2[d][idx]

            else:
                test_arr[ny][nx] = '#'
                nx += dx_2[d][idx]
                ny += dy_2[d][idx]

    return


def cctv_3(x, y, d):
    global N, M

    for idx in range(2):  
        nx = x + dx_3[d][idx]
        ny = y + dy_3[d][idx]

        while 0 <= nx < M and 0 <= ny < N and test_arr[ny][nx] != 6:
            if test_arr[ny][nx] in camera:
                nx += dx_3[d][idx]
                ny += dy_3[d][idx]

            else:
                test_arr[ny][nx] = '#'
                nx += dx_3[d][idx]
                ny += dy_3[d][idx]

    return


def cctv_4(x, y, d):
    global N, M

    for idx in range(3):  
        nx = x + dx_4[d][idx]
        ny = y + dy_4[d][idx]

        while 0 <= nx < M and 0 <= ny < N and test_arr[ny][nx] != 6:
            if test_arr[ny][nx] in camera:
                nx += dx_4[d][idx]
                ny += dy_4[d][idx]

            else:
                test_arr[ny][nx] = '#'
                nx += dx_4[d][idx]
                ny += dy_4[d][idx]

    return


def cctv_5(x, y, d):
    global N, M

    for idx in range(4):  
        nx = x + dx_5[d][idx]
        ny = y + dy_5[d][idx]

        while 0 <= nx < M and 0 <= ny < N and test_arr[ny][nx] != 6:
            if test_arr[ny][nx] in camera:
                nx += dx_5[d][idx]
                ny += dy_5[d][idx]

            else:
                test_arr[ny][nx] = '#'
                nx += dx_5[d][idx]
                ny += dy_5[d][idx]

    return


camera = [1, 2, 3, 4, 5]

# 카메라를 찾는 함수
def find():
    for y in range(N):
        for x in range(M):
            if arr[y][x] in camera:
                cameras.append([x, y, arr[y][x]])
                # perms.append([arr[y][x]])
    return


# 각각의 순열 경우의 수 (중복을 포함한다. 밑에 함수에서 중복을 없애는 작업을 할 예정)
def backtrack(k):
    if k >= len(cameras):
        perms.append(copy.deepcopy(choice))
        return

    else:
        if cameras[k][2] == 1:
            for i in range(4):
                choice[k] = i
                backtrack(k+1)

        elif cameras[k][2] == 2:
            for i in range(2):
                choice[k] = i
                backtrack(k+1)

        elif cameras[k][2] == 3:
            for i in range(4):
                choice[k] = i
                backtrack(k+1)

        elif cameras[k][2] == 4:
            for i in range(4):
                choice[k] = i
                backtrack(k+1)

        elif cameras[k][2] == 5:
            for i in range(1):
                choice[k] = i
                backtrack(k+1)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())    # N : 세로, M : 가로
    # print(N, M)

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    cameras = deque()
    find()  
    # print(cameras)    # 카메라 정보가 호출 프린트 됨  
                        # 종보는 카메라 위치, 카메라 번호

    choice = [[]] * len(cameras)
    # perms = []
    perms = deque()
    
    backtrack(0) # 순열 조합
    # print(perms)  # 중복을 포함해서 가능한 순열이 프린트 됨

    test = deque()   # 실행 하기위한 정보들을 모아서 test에 각각 리스트형식으로 담음

    blind_spot = N * M

    for try_filter in perms:
        test_arr = copy.deepcopy(arr)
        try_commend = deque()

        for try_idx in range(len(try_filter)):
            commend = copy.deepcopy(cameras[try_idx])
            commend.append(try_filter[try_idx])
            try_commend.append(commend)
        # print(try_commend)

        for test in try_commend:
            if test[2] == 1:
                cctv_1(test[0], test[1], test[3])

            elif test[2] == 2:
                cctv_2(test[0], test[1], test[3])
            
            elif test[2] == 3:
                cctv_3(test[0], test[1], test[3])
            
            elif test[2] == 4:
                cctv_4(test[0], test[1], test[3])
            
            elif test[2] == 5:
                cctv_5(test[0], test[1], test[3])

        # print(test_arr)
        test_spot = 0
        for y in range(N):
            for x in range(M):
                if test_arr[y][x] == 0:
                    test_spot += 1
        
        if test_spot < blind_spot:
            blind_spot = test_spot

    print(blind_spot)
