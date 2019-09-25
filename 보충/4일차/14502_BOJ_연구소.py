import sys, copy
sys.stdin = open('14502_BOJ_input.txt', 'r')

#   동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def virus_on(v_x, v_y):
    global N, M
    v_x -= 1
    v_y -= 1

    Q = []
    Q.append((v_x, v_y))
    test_visit[v_y][v_x] = True

    while Q:
        t_x, t_y = Q.pop(0)
        # print(Q)

        for d in range(4):
            nx = t_x + dx[d]
            ny = t_y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and test_arr[ny][nx] == 0 and test_visit[ny][nx] == False:
                Q.append((nx, ny))
                test_visit[ny][nx] = True

    return


def find_virus():
    arr_virus = []

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 2:
                arr_virus.append((x+1, y+1))

    return arr_virus


def make_combi(k, start):
    if k >= 3:
        combi.append(copy.deepcopy(choice))
        return

    else:
        for idx in range(start, len(position_0)):
            choice[k] = position_0[idx]
            make_combi(k+1, idx+1)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    # print(N, M)

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    visit = [[False] * M for _ in range(N)]
    # print(visit)

    arr_virus = find_virus()
    # print(arr_virus)

    position_0 = []
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 0:
                position_0.append((x+1, y+1))
    # print(position_0)

    choice = [''] * 3
    combi = []
    make_combi(0, 0)
    # print(combi)

    live_max = 0

    for n in range(len(combi)):
        test_arr = copy.deepcopy(arr)
        test_visit = copy.deepcopy(visit)
        live = 0

        for wall in range(3):
            wall_x, wall_y = combi[n][wall]
            test_arr[wall_y-1][wall_x-1] = 1

        for virus_xy in arr_virus:
            virus_x, virus_y = virus_xy
            virus_on(virus_x, virus_y)

        for y in range(N):
            for x in range(M):
                if test_arr[y][x] == 0 and test_visit[y][x] == False:
                    live += 1
        
        if live > live_max:
            live_max = live

    print(live_max)