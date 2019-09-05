import sys
sys.stdin = open('2005_sample_input.txt', 'r')

def pascal(k):
    global N

    if k == 1:
        arr[k-1].append(1)
        
        if k == N:
            return

        pascal(k+1)

    elif k == 2:
        arr[k-1].append(1)        
        arr[k-1].append(1)

        if k == N:
            return
        
        pascal(k+1)

    else:
        arr[k-1].append(1)
        for idx in range(1, k-1):
            arr[k-1].append(arr[k-2][idx-1] + arr[k-2][idx])
        arr[k-1].append(1)
        
        if k == N:
            return
        
        pascal(k+1)




T = int(input())
for t in range(T):
    N = int(input())
    print('#{}'.format(t+1))

    arr = [[] for _ in range(N)]

    pascal(1)

    for idx in arr:
        result = '1'
        for n in range(1, len(idx)):
            result += ' ' + str(idx[n])

        print(result)
