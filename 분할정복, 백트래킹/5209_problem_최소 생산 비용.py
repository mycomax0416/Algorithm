import sys
sys.stdin = open('5209_sample_input.txt', 'r')


def cal_cost(k, cost):
    global min_cost

    if k >= N:
        min_cost = min(min_cost, cost)
        return

    elif cost >= min_cost:
        return

    else:
        for idx in range(N):
            if visit[idx] == False:
                visit[idx] = True
                
                cal_cost(k+1, cost+arr[k][idx])
                
                visit[idx] = False


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    visit = [False for _ in range(N)]
    min_cost = 99 * N

    cal_cost(0, 0)

    print('#{} {}'.format(t+1, min_cost))