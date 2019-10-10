# import sys
# sys.stdin = open('16988_BOJ_input.txt', 'r')


def combi():
    for idx_1 in range(len(can_0)):
        pick = []
        pick.append(can_0[idx_1])
        
        for idx_2 in range(idx_1+1, len(can_0)):
            pick.append(can_0[idx_2])
            picks.append(pick[:])
            pick.pop()


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check():
    global max_result

    visit = [[False]*M for _ in range(N)]
    result = 0

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 2 and visit[y][x] == False:
                Queue = [(x, y)]
                visit[y][x] = True
                count = 1
                flag = True

                while Queue:
                    point = Queue.pop(0)
                    p_x, p_y = point[0], point[1]

                    for d in range(4):
                        nx = p_x + dx[d]
                        ny = p_y + dy[d]

                        if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 0:
                            flag = False

                        if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 2 and visit[ny][nx] == False:
                            Queue.append((nx, ny))
                            visit[ny][nx] = True
                            count += 1
                        
                if flag == False:
                    count = 0
                    break

                result += count

    max_result = max(max_result, result)



# T = int(input())
# for t in range(T):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_result = 0

can_0 = []
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            can_0.append((x, y))

picks = []
combi()

for pick in picks:
    first = pick[0]
    second = pick[1]

    arr[first[1]][first[0]] = 1
    arr[second[1]][second[0]] = 1

    check()

    arr[first[1]][first[0]] = 0
    arr[second[1]][second[0]] = 0

print(max_result)
