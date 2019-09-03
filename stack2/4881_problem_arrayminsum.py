import sys
sys.stdin = open('4881_sample_input.txt', 'r')

def backtrack(k, start):
    global result
    if k == len(arr):
        print(choice)
        result.append(choice)

    else:
        for idx in range(k, len(arr)):
            choice[k] = arr[k][idx]
            backtrack(k+1, idx+1)

T = int(input())
for t in range(1):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))

    choice = [''] * N
    result = []

    backtrack(0, 0)
    print(result)
