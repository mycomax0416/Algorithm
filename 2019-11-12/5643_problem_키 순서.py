import sys
sys.stdin = open('5643_sample_input.txt', 'r')
from collections import deque


def BFS(s):
    Q_small_to_big = deque()
    Q_small_to_big.append(s)
    visit_small_to_big = [False for _ in range(N+1)]

    while Q_small_to_big:
        p = Q_small_to_big.popleft()
        for d in small_to_big[p]:
            if visit_small_to_big[d] == False:
                Q_small_to_big.append(d)
                visit_small_to_big[d] = True
                visit[d] = True

    Q_big_to_small = deque()
    Q_big_to_small.append(s)
    visit_big_to_small = [False for _ in range(N+1)]

    while Q_big_to_small:
        p = Q_big_to_small.popleft()
        for d in big_to_small[p]:
            if visit_big_to_small[d] == False:
                Q_big_to_small.append(d)
                visit_big_to_small[d] = True
                visit[d] = True


T = int(input())
for t in range(T):
    N = int(input())
    small_to_big = [[] for _ in range(N+1)]
    big_to_small = [[] for _ in range(N+1)]

    M = int(input())
    for m in range(M):
        a, b = map(int, input().split())
        small_to_big[a].append(b)
        big_to_small[b].append(a)

    count = 0
    
    for n in range(N):
        visit = [False for _ in range(N)]
        visit.insert(0, True)
        visit[n+1] = True

        BFS(n+1)

        if False not in visit:
            count += 1

    print('#{} {}'.format(t+1, count))