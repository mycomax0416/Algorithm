import sys
sys.stdin = open('17143_BOJ_input.txt', 'r')

T = int(input())
for t in range(T):
    R, C, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    print(R, C, M)
    print(arr)