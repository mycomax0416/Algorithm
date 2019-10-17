import sys
sys.stdin = open('5251_sample_input.txt', 'r')
from collections import deque

T = int(input())
for t in range(T):
    N, E = map(int, input().split())

    G = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))

    D = [11*N for _ in range(N+1)]
    D[0] = 0
    queue = deque()
    queue.append(0)

    while queue:
        u = queue.popleft()

        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                queue.append(v)

    print('#{} {}'.format(t+1, D[N]))