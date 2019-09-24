import sys
sys.stdin = open('1486_sample_input.txt', 'r')


def cal_height(idx, height):
    global min_height

    if height >= B:
        min_height = min(min_height, height)
        return

    elif height >= min_height or idx >= N:
        return

    else:
        cal_height(idx+1, height)
        cal_height(idx+1, height+Hi[idx])


T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))

    min_height = sum(Hi)

    cal_height(0, 0)

    print('#{} {}'.format(t+1, min_height-B))