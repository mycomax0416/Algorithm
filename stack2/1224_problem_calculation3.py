import sys
sys.stdin = open('1224_sample_input.txt', 'r')

def isp(symbol):
    if symbol == ')':
        return None
    elif symbol == '*' or symbol == '/':
        return 2
    elif symbol == '+' or symbol == '-':
        return 1
    elif symbol == '(':
        return 0
    
def icp(symbol):
    if symbol == ')':
        return None
    elif symbol == '*' or symbol == '/':
        return 2
    elif symbol == '+' or symbol == '-':
        return 1
    elif symbol == '(':
        return 3

for t in range(1):
    L = int(input())
    test = list(input())
    print(test)
    transform = []
    stack = []

    while test:
        chr = test.pop(0)

        if chr.isdigit():
            transform.append(chr)

        else:
            if stack == False:
                stack.append(chr)
            
            elif icp(chr) > isp(stack[-1]):
                stack.append(chr)
        
        
        print('transform:', transform)
        print('stack:', stack)
        print('---------------')
