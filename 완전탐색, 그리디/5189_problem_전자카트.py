import sys
sys.stdin = open('5189_sample_input.txt', 'r')


def perm(k):
    if k >= len(sector):
        choice.append(1)
        combination.append(choice[:])
        choice.pop()
        return

    else:
        for i in range(len(sector)):
            if visit[i] == False:
                visit[i] = True
                choice.append(sector[i])
                
                perm(k+1)

                visit[i] = False
                choice.remove(sector[i])


def compare_path():
    global min_path

    for case in combination:
        path = 0

        for idx in range(len(case)-1):
            path += e[case[idx]-1][case[idx+1]-1]

        min_path = min(min_path, path)


T = int(input())
for t in range(T):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    sector = [n for n in range(2, N+1)]
    visit = [False for _ in range(N-1)]

    choice = [1]
    combination = []

    perm(0)

    min_path = 100 * N

    compare_path()

    print('#{} {}'.format(t+1, min_path))