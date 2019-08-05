import sys
sys.stdin = open('4831_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    arr = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))
    
    K = arr[0]
    N = arr[1]
    M = arr[2]
    count = 0
    hidden_count = 0
    location = 0
    charge_station.append(N)

    while location < N and hidden_count < N:
        hidden_count += 1
        location += K

        for k in range(len(charge_station)-1):
            if location >= charge_station[k]:
                if location < charge_station[k+1]:
                    location = charge_station[k]
                    count += 1

    if hidden_count == N:
        count = 0

    print('#{} {}'.format(i + 1, count))