import sys
sys.stdin = open('1405_BOJ_input.txt', 'r')


def perm(k):
    if k >= action:
        combinations.append(choose[:])
        return

    else:
        for option in options:
            choose.append(option)
            
            perm(k+1)
            
            choose.pop()


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def test(combination):
    global result

    visit = [[False] * 29 for _ in range(29)]
    possibility = 100

    x, y = 14, 14
    visit[y][x] = True

    for d in combination:
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 29 and 0 <= ny < 29 and visit[ny][nx] == False:
            x, y = nx, ny
            visit[ny][nx] = True

            if d == 0:
                possibility *= E/100

            elif d == 1:
                possibility *= W/100
            
            elif d == 2:
                possibility *= S/100
            
            else:
                possibility *= N/100

        else:
            return

    result += possibility
    return


action, E, W, S, N = map(int, input().split())

options = [0, 1, 2, 3]
choose = []

combinations = []
perm(0)

result = 0
for combination in combinations:
    test(combination)

print(result/100)