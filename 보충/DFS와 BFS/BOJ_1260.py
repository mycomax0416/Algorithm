import sys
sys.stdin = open('BOJ_1260_input.txt', 'r')


def DFS(start):
    stack = []
    visit = [False for _ in range(N)]
    visit.insert(0, True)
    
    stack.append(start)
    DFS_result.append(start)
    visit[start] = True

    while stack:
        node = stack[-1]
        pre_node = node

        for w in G[node]:
            if visit[w] == False:
                stack.append(w)
                DFS_result.append(w)
                visit[w] = True
                node = w
                break

        if node == pre_node:
            stack.pop()
    
    return


def BFS(start):
    Q = []
    visit = [False for _ in range(N)]
    visit.insert(0, True)

    Q.append(start)
    BFS_result.append(start)
    visit[start] = True

    while Q:
        node = Q.pop(0)

        for w in G[node]:
            if visit[w] == False:
                Q.append(w)
                BFS_result.append(w)
                visit[w] = True
        
    return

T = int(input())
for a in range(T):
    N, M, V = (map(int, input().split()))
    
    G = [[] for _ in range(N+1)]
    # print(G)

    for _ in range(M):
        v, u = map(int, input().split())
        # print(v, u)
        G[v].append(u)
        G[u].append(v)
    # print(G)

    for idx in G:
        idx.sort()
    # print(G)

    DFS_result = []
    BFS_result = []
    # DFS_output = []
    # BFS_output = []

    DFS(V)
    BFS(V)
    # print(DFS_result)
    # print(BFS_result)

    for _ in range(N):
        DFS_result.append(str(DFS_result.pop(0)))
        BFS_result.append(str(BFS_result.pop(0)))
        
    print(' '.join(DFS_result))
    print(' '.join(BFS_result))