import sys
sys.stdin = open('3234_sample_input.txt', 'r')

def swim(n, cost):
    global ans
    if n >= 12:
        ans = min(ans, cost)
        return

    if arr[n] == 0:
        swim(n+1, cost)

    else:
        swim(n+1, cost+day*arr[n])
        swim(n+1, cost+month)
        swim(n+3, cost+quarter)


T = int(input())
for t in range(T):
    day, month, quarter, year = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = year

    swim(0, 0)

    print('#{} {}'.format(t+1, ans))