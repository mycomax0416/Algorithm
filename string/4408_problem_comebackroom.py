import sys
sys.stdin = open('4408_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N = int(input())
    empty = [0] * 400
    result = 0
    
    for _ in range(N):
        first, last = map(int, input().split())
        
        if first > last:
            first, last = last, first

        if first % 2 == 0:
            first -= 1
        
        if last % 2 == 1:
            last += 1

        for point in range(first, last):
            empty[point] += 1

    for idx in empty:
        if idx > result:
            result = idx

    print('#{} {}'.format(i+1, result))