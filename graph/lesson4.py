#from collections import deque
import sys
sys.stdin = open('lesson2.txt', 'r')

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]    # 1 ~ V
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))


# def BFS(s):
#     Q = deque()
#     D = [0xffffffff] * (V+1)    # D[] 배열 초기값설정, 
#     D[s] = 0                    # 출발점의 D 값을 0으로 설정
#     Q.append(s)
#     while Q:
#         u = Q.popleft()
#         for v, w in G[u]:
#             if D[v] > D[u] + w:
#                 D[v] = D[u] + w
#                 Q.append(v)


def dijkstra(s):
    D = [0xffffffff] * (V+1)    # D[] 배열 초기값설정, 
    D[s] = 0                    # 출발점의 D 값을 0으로 설정
    visit = [False] * (V+1)     # 최단 경로를 찾은 정점들과 아닌 정점들
    cnt = V
    while cnt:
        u, MIN = 0, 0xfffffffffff
        for i in range(1, V+1):     # D값이 최소인 정점을 찾는다.
            if not visit[i] and MIN > D[i]:
                u, MIN = i, D[i]
        visit[u] = True
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
        cnt -= 1


# BFS(1)

dijkstra(1)