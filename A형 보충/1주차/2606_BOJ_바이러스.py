import sys
sys.stdin = open('2606_BOJ_input.txt', 'r')


def DFS(start):
    stack = []
    stack.append(start)
    visit[start] = True

    while stack:
        v = stack[-1]
        pre_v = v

        for w in G[v]:
            if visit[w] == False:
                stack.append(w)
                visit[w] = True
                v = w
                break

        if pre_v == v:
            stack.pop()


computer = int(input())
pair = int(input())

G = [[] for _ in range(computer+1)]
visit = [False for _ in range(computer+1)]

for i in range(pair):
    n, m = map(int, input().split())
    G[n].append(m)
    G[m].append(n)

DFS(1)

count = -1
for test in visit:
    if test == True:
        count += 1

print(count)
