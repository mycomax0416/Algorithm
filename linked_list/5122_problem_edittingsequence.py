import sys
sys.stdin = open('5122_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    result = -1

    for m in range(M):
        info = input().split()
        if info[0] == 'I':
            arr.insert(int(info[1]), int(info[2]))
        
        elif info[0] == 'D':
            arr.pop(int(info[1]))

        elif info[0] == 'C':
            arr[int(info[1])] = int(info[2])
    
    if L < len(arr):
        result = arr[L]

    print('#{} {}'.format(t+1, result))
