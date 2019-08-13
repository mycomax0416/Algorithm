import sys
sys.stdin = open('1946_sample_input.txt', 'r')

T = int(input())

for i in range(1):
    N = int(input())
    
    result = ''

    for j in range(N):
        test_alpha, test_num = input().split()
        
        # print(test_alpha, test_num)
        result += test_alpha * int(test_num)
        
    # print(result)
    for k in range(len(result)):
        if k % 9 == 9:
            print(result[k], end='\n')
        else:
            print(result[k], end='')
