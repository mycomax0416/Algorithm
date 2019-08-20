import sys
sys.stdin = open('4873_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    words = list(map(str, input()))
    count = 0
    stack = [None, None]
    
    for word in words:
        stack += word
        
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    print('#{} {}'.format(i+1, len(stack)-2))
