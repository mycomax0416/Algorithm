import sys
sys.stdin = open('1.txt', 'r')
from collections import deque

# 2기 보충 수업
# 1260 DFS, BFS 백준

# 1기
# 11724 연결 요소의 개수 DFS로 해결
# 2667 단지번호붙이기 DFS로 해결?
# 2178 미로 탐색 BFS로 해결?
# 2206 벽 부수고 이동하기 BFS로 해결

# 밑에 문제는 Page: 197 연습문제 3

def BFS(s):     # s: 시작점
    # 큐를 생성
    # 시작점을 방문하고, 큐에 삽입

    # 빈 큐가 아닐 동안
        # v: 큐에 정점을 하나 꺼내온다.
        # v의 방문하지 않은 인접 정점 w를 찾는다.
            # w를 방문하고 큐에 삽입

    Q = deque()
    D[s], P[s] = 0, s
    visit[s] = True; print(s, end=' ')
    Q.append(s)
    while Q: # 빈 큐가 아닐 동안
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = True; [print(w, end=' ')]
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)
    
    print(P)
    print(D)


#------------------------------------------------------
V, E = map(int, input().split())    # 정점수, 간선수

G = [[] for _ in range(V + 1)]  # 정점번호 1 ~ V
visit = [False] * (V + 1)       # 방문정보

D = [0] * (V + 1)
P = [0] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u) # 무향 그래프

BFS(1)