import sys
sys.stdin = open('7465_sample_input.txt', 'r')


def BFS(start):
    Q = []
    Q.append(start)
    visit[start] = True

    while Q:
        w = Q.pop(0)

        for v in G[w]:
            if visit[v] == False:
                visit[v] = True
                Q.append(v)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    visit = [False for _ in range(N+1)]

    for m in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    group = 0
    for n in range(1, N+1):
        if visit[n] == False:
            group += 1
            BFS(n)

    print('#{} {}'.format(t+1, group))