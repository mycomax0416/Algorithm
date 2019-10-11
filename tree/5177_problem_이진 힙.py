import sys
sys.stdin = open('5177_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(N)
    print(arr)