import sys
sys.stdin = open('2805_sample_input.txt', 'r')


def cut():
    for n in range(N//2):
        for _ in range(N//2 - n):
            arr[n].pop(0)
            arr[n].pop()

    for m in range(N-1, N//2-1, -1):
        for _ in range(m - N//2):
            arr[m].pop(0)
            arr[m].pop()


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]

    cut()

    result = 0
    for row in arr:
        result += sum(row)

    print('#{} {}'.format(t+1, result))
