import sys
sys.stdin = open('4864_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    standard = input()
    compare = input()

    n, m = 0, 0
    while n < len(compare) and m < len(standard):
        if compare[n] != standard[m]:
            n = n - m
            m = -1
        n += 1
        m += 1
       
        if len(standard) == m:
            print('#{} {}'.format(i + 1, '1'))
            break
        
        if len(compare) == n:
            print('#{} {}'.format(i + 1, '0'))