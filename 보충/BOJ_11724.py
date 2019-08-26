import sys
sys.stdin = open('BOJ_11724_input.txt', 'r')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    G = [[] for _ in range(N+1)]
    visit = [True]
    visit += [False for _ in range(N)]
    count = 0

    for _ in range(M):
        u, v = map(int, input().split())
        G[u] += [v]
        G[v] += [u]
    
    while visit != [True for _ in range(N+1)]:
        for i in range(len(visit)):
            if not visit[i]:
                s = i
                break

        stack = []
        v = s
        stack += [v]
        visit[v] = True

        while len(stack) > 0:
            prev = v
            for w in G[v]:
                if not visit[w]:
                    stack += [w]
                    visit[w] = True
                    v = w
                    break
            
            if prev == v:
                v = stack.pop()

        count += 1

    print(count)
