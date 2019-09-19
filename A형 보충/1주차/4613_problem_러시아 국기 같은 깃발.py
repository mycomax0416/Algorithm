import sys
sys.stdin = open('4613_sample_input.txt', 'r')

T = int(input())
for t in range(1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(arr)