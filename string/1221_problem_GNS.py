import sys
sys.stdin = open('1221_sample_input.txt', 'r')

numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for i in range(T):
    test_num, test_len = input().split()
    test = list(input().split())
    
    result = []

    for j in numbers:
        for k in test:
            if j == k:
                result += [k]
    
    print('#{}\n{}'.format(i + 1, ' '.join(result)))