import sys
sys.stdin = open('1697_BOJ_input.txt', 'r')


def BFS(s):
    Q = []
    visit = [False for _ in range(100000)]
    
    Q.append(s)
    visit[s] = True

    while Q:
        location = Q.pop(0)
        count += 1
        
        if location == K:
            break



N, K = map(int, input().split())

count = 0

BFS(N)