T = int(input())

for tc in range(T):
    N, M, K = (map(int, input().split()))

    arr = []

    for _ in range(N):
        arr += [list(map(int, input().split()))]

    num = []

    for y in range(N-K+1):
        for x in range(M-K+1):
            tc_sum = 0
            
            for py in range(K):
                for px in range(K):
                    tc_sum += arr[y+py][x+px]

            for my in range(K-2):
                for mx in range(K-2):
                    tc_sum -= arr[y+1+my][x+1+mx]

            num += [tc_sum]
    
    print('#{} {}'.format(tc+1, max(num)))