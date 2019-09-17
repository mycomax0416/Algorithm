import sys
sys.stdin = open('5203_sample_input.txt', 'r')


def babyjin():
    global player_1, player_2

    for idx in range(10):
        if idx < 7:
            if arr_1[idx] != 0 and arr_1[idx+1] != 0 and arr_1[idx+2] != 0:
                player_1 = 'run'
            if arr_2[idx] != 0 and arr_2[idx+1] != 0 and arr_2[idx+2] != 0:
                player_2 = 'run'

        if arr_1[idx] == 3:
            player_1 = 'triplet'
        if arr_2[idx] == 3:
            player_2 = 'triplet'


T = int(input())
for t in range(1):
    arr = list(map(int, input().split()))

    player_1 = 0
    player_2 = 0

    arr_1 = [0 for n in range(10)]
    arr_2 = [0 for n in range(10)]

    for idx in range(0, len(arr), 2):
        arr_1[arr[idx]] += 1
        arr_2[arr[idx+1]] += 1

        babyjin()

        print(player_1, player_2)

    # print(arr_1)
    # print(arr_2)