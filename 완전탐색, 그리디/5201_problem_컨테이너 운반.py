import sys
sys.stdin = open('5201_sample_input.txt', 'r')


def docker(k, weight):
    global max_weight

    if k >= M:
        max_weight = max(max_weight, weight)
        return

    else:
        exist = False
        for idx in range(N):
            if check[idx] == False and ti[k] >= wi[idx]:
                pre_idx = idx
                check[idx] = True
                exist = True
                break
        
        if exist == True:
            for idx in range(N):
                if check[idx] == False and ti[k] >= wi[idx] > wi[pre_idx]:
                    check[pre_idx] = False
                    check[idx] = True

                    pre_idx = idx

            docker(k+1, weight+wi[pre_idx])
        
        else:
            docker(k+1, weight)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    check = [False for _ in range(N)]

    max_weight = 0

    docker(0, 0)

    print('#{} {}'.format(t+1, max_weight))