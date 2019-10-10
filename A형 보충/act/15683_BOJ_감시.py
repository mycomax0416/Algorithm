import sys
sys.stdin = open('15683_BOJ_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(N, M)
    print(arr)