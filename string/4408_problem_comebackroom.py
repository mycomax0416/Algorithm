import sys
sys.stdin = open('4408_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N = int(input())
    standard = [0] * 400
    arr = []
    
    for j in range(N):
        arr += [list(map(int, input().split()))]

    for l in range(len(arr)):
        if arr[l][0] % 2 == 0:
            arr[l][0] -= 1
        
        if arr[l][1] % 2 == 1:
            arr[l][1] += 1
    
    arr += ['point']
    count = 0

    while arr != ['point']:
        compare = arr.pop(0)
        if compare == 'point':
            count += 1
            arr += ['point']
            standard = [0] * 401

        elif standard[compare[0]] == 0 and standard[compare[1]] == 0:
            for k in range(compare[0], compare[1]):
                standard[k] = 1

        else:
            arr += [compare]
        print(compare)
        print(arr)
        print(standard)
    
    count += 1
    print('#{} {}'.format(i+1, count))
