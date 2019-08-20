import sys
sys.stdin = open('4871_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    V, E = map(int, input().split())
   
    path = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]
    
    for j in range(E):
        u, v = map(int, input().split())
        path[u] += [v]

    S, G = map(int, input().split())
    
    stack = []
    stack += [S]
    visit[S] = True
    result = 0

    while len(stack) > 0:
        pre = S

        if S == G:
            result = 1
            break

        for w in path[S]:
            if not visit[w]:
                stack += [w]
                S = w
                visit[w] = True
                break

        if pre == S:
            S = stack.pop()

    print('#{} {}'.format(i+1, result))

