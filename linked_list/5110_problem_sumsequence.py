import sys
sys.stdin = open('5110_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = ''

    for m in range(M-1):
        insert_arr = list(map(int, input().split()))
        for idx, val in enumerate(arr):
            if val > insert_arr[0]:
                while insert_arr:
                    arr.insert(idx, insert_arr.pop())
                break
        
        if insert_arr:
            while insert_arr:
                arr.append(insert_arr.pop(0))

    for _ in range(10):
        result += ' ' + str(arr.pop())

    print('#{}{}'.format(t+1, result))
