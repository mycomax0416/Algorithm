import sys
sys.stdin = open('4874_sample_input.txt', 'r')

T = int(input())

for t in range(T):
    arr = list(input().split())
    stack = []
    result = 0
    idx = 0
    
    while arr[idx] != '.':
        if arr[idx].isdigit():
            stack += [int(arr[idx])]
        
        elif arr[idx] == '+' and len(stack) >= 2:
            first = stack.pop()
            second = stack.pop()
            stack += [second + first]

        elif arr[idx] == '-' and len(stack) >= 2:
            first = stack.pop()
            second = stack.pop()
            stack += [second - first]

        elif arr[idx] == '*' and len(stack) >= 2:
            first = stack.pop()
            second = stack.pop()
            stack += [second * first]

        elif arr[idx] == '/' and len(stack) >= 2:
            first = stack.pop()
            second = stack.pop()
            stack += [second // first]

        else:
            stack += ['error']
            break

        idx += 1

    if len(stack) >= 2:
        stack += ['error']

    print('#{} {}'.format(t+1, stack[-1]))
