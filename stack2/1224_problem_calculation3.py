import sys
sys.stdin = open('1224_sample_input.txt', 'r')

icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

for test_case in range(1, 11):
    N = int(input())
    infix = input()
    postfix = ''

    S = []

    for ch in infix:
        if ch == ')':
            while S[-1] != '(':
                postfix += S.pop()
            S.pop()
        elif ch in icp:
            if len(S) == 0:
                S.append(ch)
                continue

            while len(S) and isp[S[-1]] >= icp[ch]:
                postfix += S.pop()
            S.append(ch)
        else:
            postfix += ch

    while len(S) > 0:
        postfix += S.pop()


    S = []
    for ch in postfix:
        if ch in isp:
            b, a = S.pop(), S.pop()
            if ch == '+':
                S.append(a + b)
            elif ch == '-':
                S.append(a - b)
            elif ch == '*':
                S.append(a * b)
            else:
                S.append(a // b)
        else:
            S.append(int(ch))

    print("#%d %d" % (test_case, S[0]))

#---------------------------------------------
# def isp(symbol):
#     if symbol == ')':
#         return None
#     elif symbol == '*' or symbol == '/':
#         return 2
#     elif symbol == '+' or symbol == '-':
#         return 1
#     elif symbol == '(':
#         return 0
    
# def icp(symbol):
#     if symbol == ')':
#         return None
#     elif symbol == '*' or symbol == '/':
#         return 2
#     elif symbol == '+' or symbol == '-':
#         return 1
#     elif symbol == '(':
#         return 3

# for t in range(1):
#     L = int(input())
#     test = list(input())
#     print(test)
#     transform = []
#     stack = []

#     while test:
#         chr = test.pop(0)

#         if chr.isdigit():
#             transform.append(chr)

#         else:
#             if stack == False:
#                 stack.append(chr)
            
#             elif icp(chr) > isp(stack[-1]):
#                 stack.append(chr)
        
        
#         print('transform:', transform)
#         print('stack:', stack)
#         print('---------------')
