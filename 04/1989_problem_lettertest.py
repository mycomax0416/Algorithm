import sys
sys.stdin = open('1989_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    test = input()
    
    if test == test[::-1]:
        print('#{} {}'.format(i + 1, 1))
    else:
    	print('#{} {}'.format(i + 1, 0))