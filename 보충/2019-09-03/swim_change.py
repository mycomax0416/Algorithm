import sys
sys.stdin = open('input.txt', 'r')

def backtrack(n, cost):
    global ans
    if n >= 12:
        ans = min(ans, cost)
        return

    if arr[n] == 0:
        backtrack(n + 1, cost)

    else:
        backtrack(n + 1, cost + day * arr[n])
        backtrack(n + 1, cost + month)
        backtrack(n + 3, cost + quarter)



T = int(input())
for t in range(T):
    day, month, quarter, year = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = year

    backtrack(0, 0)

    print('#{} {}'.format(t+1, ans))