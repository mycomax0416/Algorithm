import sys, copy
sys.stdin = open('1865_sample_input.txt', 'r')


def comb(k):
    global cal, max_problitiy

    if k >= N:
        max_problitiy = max(max_problitiy, cal)
        return

    elif cal < max_problitiy:
        return

    else:
        for i in range(N):
            if visit[i] == False:
                if arr[k][i] != 0:
                    cal *= arr[k][i]/100
                    visit[i] = True

                    comb(k+1)
                    
                    cal /= arr[k][i]/100
                    visit[i] = False
        

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [False for _ in range(N)]

    max_problitiy = 0
    cal = 100

    comb(0)
    
    print('#{}'.format(t+1), '%.6f' % max_problitiy)