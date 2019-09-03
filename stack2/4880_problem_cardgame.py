import sys
sys.stdin = open('4880_sample_input.txt', 'r')

win = {1: 3, 2: 1, 3: 2}

def play(lo, hi):
    if lo == hi:
        return lo

    mid = (lo + hi)//2
    
    l = play(lo, mid)
    r = play(mid + 1, hi)

    if cards[l] == cards[r] or win[cards[l]] == cards[r]:
        return l

    return r


T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    
    result = play(0, len(cards)-1) + 1

    print('#{} {}'.format(t+1, result))
