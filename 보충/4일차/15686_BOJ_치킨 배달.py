import sys
sys.stdin = open('15686_BOJ_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    print(N, M)

    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))

    print(arr)
