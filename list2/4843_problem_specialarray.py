import sys
sys.stdin = open('4843_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    result = []
    count = 0
    
    while count < 10:
        count += 2

        arr_max = arr[0]
        arr_min = arr[0]
        max_idx = 0
        min_idx = 0

        for k in range(len(arr)):
            if arr[k] > arr_max:
                arr_max = arr[k]
                max_idx = k
        result += [str(arr.pop(max_idx))]
        
        for l in range(len(arr)):
            if arr[l] < arr_min:
                arr_min = arr[l]
                min_idx = l
        result += [str(arr.pop(min_idx))]

    # print('#{} {}'.format(i + 1, ' '.join(result)))
    print('#{} '.format(i + 1) + ' '.join(result))