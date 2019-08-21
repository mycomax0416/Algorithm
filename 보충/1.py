import sys
sys.stdin = open('1.txt', 'r')

def DFS(v): # v: 현재 방문하는 정점, 시작점
    # v를 방문하고
    # v의 방문하지 않은 인접정점을 G[v]에서 찾는다.
    # 재귀호출한다.
    visit[v] = True; print(v, end=' ')
    for w in G[v]:
        if not visit[w]:
            DFS(w)






V, E = map(int, input().split())    # 정점수, 간선수

G = [[] for _ in range(V + 1)]  # 정점번호 1 ~ V
visit = [False] * (V + 1)       # 방문정보

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u) # 무향 그래프

# print(G)
for i in range(1, V + 1):
    print(i, '-->', G[i])

DFS(1)