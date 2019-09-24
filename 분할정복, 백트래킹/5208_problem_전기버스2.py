import sys
sys.stdin = open('5208_sample_input.txt', 'r')


def bus(count, battery, start):
    global change_min

    if start >= N-1:
        change_min = min(change_min, count)
        return

    elif battery <= 0:
        return

    elif count >= change_min:
        return

    else:
        bus(count, battery-1, start+1)
        bus(count+1, Mi[start+1], start+1)


T = int(input())
for t in range(T):
    Mi = list(map(int, input().split()))
    Mi.append(0)
    N = Mi.pop(0)

    change_min = N

    bus(0, Mi[0], 0)
    print('#{} {}'.format(t+1, change_min))