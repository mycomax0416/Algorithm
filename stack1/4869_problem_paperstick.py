import sys
sys.stdin = open('4869_sample_input.txt', 'r')

def function(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return function(n-1) + function(n-2) * 2
    
T = int(input())

for i in range(T):
    N = int(input())
    
    print('#{} {}'.format(i + 1, function(N//10)))



