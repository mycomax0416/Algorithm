import sys
sys.stdin = open('4875_sample_input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    global ans
    S.append((x, y))
    visit[x][y] = 1
    
    while S:
        print(S)
        x, y = S.pop()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < N and 0 <= ny <N and visit[nx][ny] == 0:
                if arr[nx][ny] == 3:
                    ans = 1
                    return
                if arr[nx][ny] == 0:
                    S.append((nx, ny))
                    visit[nx][ny] = 1
def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                DFS(i,j)
                return

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for i in range(N)]

    S = []
    visit = [[0]*N for _ in range(N)]
    ans = 0

    find()

    print('#{} {}'.format(case, ans))
