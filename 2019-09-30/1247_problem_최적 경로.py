import sys
sys.stdin = open('1247_sample_input.txt', 'r')


def backtrack(x, y, k, r):
    global min_r

    if k >= N:
        r += abs(x-home[0]) + abs(y-home[1])
        min_r = min(min_r, r)
        return

    elif r >= min_r:
        return

    else:
        for customer in customers:
            if visit[customer[1]][customer[0]] == False:
                visit[customer[1]][customer[0]] = True

                backtrack(customer[0], customer[1], k+1, r+(abs(x-customer[0])+abs(y-customer[1])))

                visit[customer[1]][customer[0]] = False


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    company = arr.pop(0), arr.pop(0)
    home = arr.pop(0), arr.pop(0)
    customers = []
    for _ in range(N):
        customers.append((arr.pop(0), arr.pop(0)))

    visit = [[False] * 101 for _ in range(101)]
    min_r = 200 * (N+1)
    
    backtrack(company[0], company[1], 0, 0)

    print('#{} {}'.format(t+1, min_r))