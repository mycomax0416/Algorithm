import sys
sys.stdin = open('4835_sample_input.txt', 'r')

T = input()

for i in range(int(T)):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    near_sum = [0] * (len(arr)-(M-1))

    for n in range(len(arr)-(M-1)):
        for m in range(M):
            near_sum[n] += arr[n+m]

    my_max = near_sum[0]
    my_min = near_sum[0]

    for x in range(1, len(near_sum)):
        if near_sum[x] > my_max:
            my_max = near_sum[x]
        if near_sum[x] < my_min:
            my_min = near_sum[x]

    print('#{} {}'.format(i+1, my_max-my_min))