import sys
sys.stdin = open('4880_sample_input.txt', 'r')

def game(arr):
    if len(arr) < 2:
        return 0


    if len(arr) == 2:
        if sum(arr) == 3:
            print(2)

        if sum(arr) == 4:
            print(1)

        if sum(arr) == 5:
            print(3)
    else:
        return game(arr[0:len(arr)//2]) + game(arr[len(arr)//2:])


T = int(input())

for t in range(1):
    N = int(input())
    # print(N)

    arr = list(map(int, input().split()))

    # print(arr[0:len(arr)//2])
    # print(arr[len(arr)//2:])
    game(arr)
