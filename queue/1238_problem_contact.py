import sys
sys.stdin = open('1238_sample_input.txt', 'r')

def BFS(s):
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

for t in range(10):
    L, S = map(int, input().split())

    G = [[] for _ in range(101)]
    visit = [False for _ in range(101)]

    arr = list(map(int, input().split()))
    for _ in range(len(arr)//2):
        v, u = arr.pop(0), arr.pop(0)
        G[v].append(u)

    D = [0] * 101

    BFS(S)

    max_val = 0
    for idx, val in enumerate(D):
        if val >= max_val:
            max_val = val
            last = idx

    print('#{} {}'.format(t+1, last))
