import sys
sys.stdin = open('3752_sample_input.txt', 'r')


def function(arr):
    result = set([0])
    
    for i in arr:
        for j in list(result):
            result.add(i+j)
    
    return len(result)


T  = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(t+1, function(arr)))