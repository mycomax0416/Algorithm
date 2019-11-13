import sys
sys.stdin = open('2117_sample_input.txt', 'r')
from pprint import pprint

T = int(input())
for t in range(1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint(arr)

    for y in range(N):
        for x in range(N):
            count = 0
            if arr[y][x] == 1:
                count += 1
            # for test in range(2N, -1):
            #     print(test)
    for test in range(2*N, 0, -1):
        print(test)