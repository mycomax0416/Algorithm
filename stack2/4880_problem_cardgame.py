import sys
sys.stdin = open('4880_sample_input.txt', 'r')

def game(arr):
    if len(arr) == 1:
        return arr[0]

    elif len(arr) == 2:
        if arr[0][0] == 1 and arr[1][0] == 2:
            return arr[1]
        elif arr[0][0] == 2 and arr[1][0] == 1:
            return arr[0]

        elif arr[0][0] == 1 and arr[1][0] == 3:
            return arr[0]
        elif arr[0][0] == 3 and arr[1][0] == 1:
            return arr[1]

        elif arr[0][0] == 2 and arr[1][0] == 3:
            return arr[1]
        elif arr[0][0] == 3 and arr[1][0] == 2:
            return arr[0]

        elif arr[0][0] == 1 and arr[1][0] == 1: # 비길때
            return arr[0]
        elif arr[0][0] == 2 and arr[1][0] == 2:
            return arr[0]
        elif arr[0][0] == 3 and arr[1][0] == 3:
            return arr[0]

    elif len(arr) == 3:
        return game([arr[0], game([arr[1], arr[2]])])

    elif len(arr) > 3:
        return game([game(arr[0:len(arr)//2]), game(arr[len(arr)//2:])])

T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for no in range(1, len(arr)+1):
        arr += [[arr.pop(0), no]]

    print('#{} {}'.format(t+1, game(arr)[1]))