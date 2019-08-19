import sys
sys.stdin = open('back_10815_sample.txt', 'r')

N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

for m in M_arr:
    if m in N_arr:
        print(1, end=' ')
    else:
        print(0, end=' ')