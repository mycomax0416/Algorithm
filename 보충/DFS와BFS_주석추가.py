from collections import deque

N, M, V = (map(int, input().split()))

# print(N, M, V)

old_G = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    old_G[u] += [v]
    old_G[v] += [u]

# print(old_G)
# -----------------------
new_G = []
for tc in old_G:
    if tc != []:
        new_arr = []
        for _ in range(len(tc)):
            new_arr += [min(tc)]
            tc.remove(min(tc))
        new_G += [new_arr]
    else:
        new_G += [[]]

# print(new_G)
# -----------------------
BFS = []
v = V
stack = []
stack += [v]
visit[v] = True
BFS += [v]

while len(stack) > 0:
    prev = v
    for w in new_G[v]:
        if not visit[w]:
            stack += [v]    # <--- 틀린곳!!!!!!!!!!!!!!!!
            visit[w] = True
            v = w
            BFS += [v]
            break

    if prev == v:
        v = stack.pop()

# print(BFS)

# --------------------------DFS
DFS = []
Q = deque()
visit = [False for _ in range(N + 1)]
D = [0 for _ in range(N + 1)]
P = [0 for _ in range(N + 1)]

s = V
D[s] = 0
P[s] = s
visit[s] = True

DFS += [s]
Q += [s]
while Q:
    v = Q.popleft()
    for w in new_G[v]:
        if not visit[w]:
            visit[w] = True
            DFS += [w]
            D[w] = D[v] + 1
            P[w] = v
            Q.append(w)

print(' '.join(list(map(str, BFS))))
print(' '.join(list(map(str, DFS))))
#----------------------------------------------------------
#  정리한 코드
#----------------------------------------------------------

from collections import deque

N, M, V = (map(int, input().split()))
G = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u] += [v]
    G[v] += [u]

for lst in G:       # 정렬하기
    lst.sort()

BFS = []
v = V
stack = [v]
visit[v] = True
BFS += [v]

while len(stack) > 0:
    for w in G[v]:
        if not visit[w]:
            stack += [v]
            visit[w] = True
            v = w
            BFS += [v]
            break
    else:
        v = stack.pop()

# --------------------------DFS
Q = deque()
visit = [False for _ in range(N + 1)]

s = V
visit[s] = True
DFS = [s]
Q += [s]

while Q:
    v = Q.popleft()
    for w in G[v]:
        if not visit[w]:
            visit[w] = True
            DFS += [w]
            Q.append(w)

print(' '.join(list(map(str, BFS))))
print(' '.join(list(map(str, DFS))))

