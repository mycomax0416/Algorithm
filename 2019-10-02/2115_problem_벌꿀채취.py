import sys
sys.stdin = open('2115_sample_input.txt', 'r')


def comb(k, n, s):
    if k >= M:
        if n <= C:
            cal_test.append(s)
        return
    
    else:
        comb(k+1, n, s)
        comb(k+1, n+test[k], s+test[k]**2)


T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    select = [[False] * N for _ in range(N)]

    profits = set()

    for y in range(N):
        for x in range(N-M+1):
            test = []

            for s_x in range(x, x+M):
                select[y][s_x] = True
                test.append(arr[y][s_x])

            cal_test = []
            comb(0, 0, 0)
            max_test_1 = max(cal_test)                      
            #----------------------------------------
            for j in range(N):
                for i in range(N-M+1):
                    test = []

                    for s_i in range(i, i+M):
                        if select[j][s_i] == True:
                            break
                    
                        test.append(arr[j][s_i])

                    if len(test) == M:
                        cal_test = []
                        comb(0, 0, 0)
                        max_test_2 = max(cal_test)
                        profits.add(max_test_1+max_test_2)
            #----------------------------------------
            for s_x in range(x, x+M):
                select[y][s_x] = False

    print('#{} {}'.format(t+1, max(profits)))