import sys
sys.stdin = open('5102_sample_input.txt', 'r')

def BFS(s, f):
    Q = []
    Q.append(s)
    visit[s] = True

    while Q:
        v = Q.pop(0)

        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                Q.append(w)
                D[w] = D[v] + 1

    return D[f]


T = int(input())
for t in range(T):
    V, E = map(int, input().split())

    G = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]

    for _ in range(E):
        v, u = map(int, input().split())
        G[v].append(u)
        G[u].append(v)

    S, F = map(int, input().split())
    D = [0] * (V+1)

    print('#{} {}'.format(t+1, BFS(S, F)))
