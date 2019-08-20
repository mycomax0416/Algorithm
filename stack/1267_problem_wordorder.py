import sys
sys.stdin = open('1267_sample_input.txt', 'r')

for i in range(10):
    V, E = map(int, input().split())
    lines = list(map(int, input().split()))

    path = [[] for _ in range(V+1)]
    visit = [True]
    visit += [False for _ in range(V)]

    for j in range(E):
        u, v = lines.pop(0), lines.pop(0)
        path[v] += [u]

    result = []

    while False in visit:
        for k in range(1, len(path)):
            if path[k] == [] and visit[k] == False:
                S = k
                visit[S] = True
                result += [S]
                break

        for n in path:
            if S in n:
                n.remove(S)
    
    final = list(map(str, result))
    print('#{} {}'.format(i+1, ' '.join(final)))
