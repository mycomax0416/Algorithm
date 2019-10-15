import sys
sys.stdin = open('5248_sample_input.txt', 'r')
from collections import deque


def grouping():
    global group

    visit = [False for _ in range(N+1)]

    for n in range(N+1):
        if visit[n] == False:
            queue = deque()
            queue.append(n)
            group += 1

            while queue:
                test = queue.popleft()

                for idx in G[test]:
                    if visit[idx] == False:
                        queue.append(idx)
                        visit[idx] = True


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    G = [[] for _ in range(N+1)]
    for idx in range(len(arr)//2):
        G[arr[2*idx]].append(arr[2*idx+1])
        G[arr[2*idx+1]].append(arr[2*idx])

    group = 0
    grouping()

    print('#{} {}'.format(t+1, group-1))