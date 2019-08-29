import sys
sys.stdin = open('5099_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    for no in range(M):
        Ci.append((Ci.pop(0), no+1))

    in_pizza = Ci[0:N]
    out_pizza = Ci[N:]
    stack = []

    while len(stack) != M:
        amount, no = in_pizza.pop(0)
        if amount > 1:
            amount //= 2
            in_pizza.append((amount, no))
    
        elif amount == 1:
            if out_pizza:
                stack.append((amount, no))
                in_pizza.append(out_pizza.pop(0))

            else:
                stack.append((amount, no))

    print('#{} {}'.format(t+1, stack[-1][-1]))
