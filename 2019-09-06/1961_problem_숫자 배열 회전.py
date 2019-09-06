import sys
sys.stdin = open('1961_sample_input.txt', 'r')


def func_90():
    global N
    idx = -1

    for x in range(N):
        line = ''
        idx += 1

        for y in range(N-1, -1, -1):
            line += str(arr[y][x])

        result[idx].append(line)
    
    return


def func_180():
    global N
    idx = -1

    for y in range(N-1, -1, -1):
        line = ''
        idx += 1

        for x in range(N-1, -1, -1):
            line += str(arr[y][x])

        result[idx].append(line)

    return


def func_270():
    global N
    idx = -1

    for x in range(N-1, -1, -1):
        line = ''
        idx += 1

        for y in range(N):
            line += str(arr[y][x])

        result[idx].append(line)

    return


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = [[] for _ in range(N)]

    func_90()
    func_180()
    func_270()

    print('#{}'.format(t+1))

    for n in range(N):
        print(' '.join(result[n]))
