import sys
sys.stdin = open('5249_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    V, E = map(int, input().split())

    G = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1].append((n2, w))
        G[n2].append((n1, w))

    key = [11 for _ in range(V+1)]
    key[0] = 0

    count = V+1
    visit = [False for _ in range(V+1)]
    result = 0
    
    while count:
        min_len = 11

        for idx in range(V+1):
            if not visit[idx] and min_len > key[idx]:
                u, min_len = idx, key[idx]

        visit[u] = True
        result += key[u]

        for v, w in G[u]:
            if not visit[v] and w < key[v]:
                key[v] = w

        count -= 1

    print('#{} {}'.format(t+1, result))