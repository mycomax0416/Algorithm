import sys
sys.stdin = open('4408_sample_input.txt', 'r')

T = int(input())

for i in range(1):
    N = int(input())
    standard = [0] * 400
    arr = []
    
    for j in range(N):
        arr += [list(map(int, input().split()))]

    for k in range(len(arr)):
        if arr[k][0] != 1 and arr[k][1] != 1:
            if arr[k][0]//2 == 1:
                first = arr[k][0]
            else:
                first = arr[k][0] - 1

            if arr[k][1]//2 == 1:
                second = arr[k][1] + 1
            else:
                second = arr[k][1]

            for l in range(first, second):
                standard[l] = 1
        
    # print(arr)
    # print(standard)

