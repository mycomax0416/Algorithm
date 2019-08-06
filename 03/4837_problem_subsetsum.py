import sys
sys.stdin = open('4837_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N, K = list(map(int, input().split()))
    
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = []
    count = 0
    len_arr = len(arr)

    for j in range(1<<len_arr):
        pick = []
        for n in range(len_arr):
            if j & (1<<n):
                pick += [arr[n]]
        if len(pick) == N:
            result += [pick]

    for m in result:
        if sum(m) == K:
            count += 1
            
    print('#{} {}'.format(i + 1, count))




