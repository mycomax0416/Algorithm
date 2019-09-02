import sys
sys.stdin = open('5108_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    sequence = list(map(int, input().split()))

    for m in range(M):
        idx, num = map(int, input().split())
        sequence.insert(idx, num)

    print('#{} {}'.format(t+1, sequence[L]))
