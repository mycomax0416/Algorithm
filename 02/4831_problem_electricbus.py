import sys
sys.stdin = open('4831_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    arr_1 = list(map(int, input().split()))
    charge_station = list(map(int, input().split()))

    K = arr_1[0]
    N = arr_1[1]
    M = arr_1[2]
    count = 0
    hidden_count = 0
    location = 0
    charge_station.append(100)

    while location < N and hidden_count < 100:
        hidden_count += 1

        for k in range(len(charge_station)-1):
            if location >= charge_station[k]:
                if location < charge_station[k+1]:
                    location = charge_station[k]
                    count += 1

        location += K

    if hidden_count == 100:
        count = 0

    print('#{} {}'.format(i + 1, count))