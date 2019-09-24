import sys
sys.stdin = open('2817_sample_input.txt', 'r')


def function(k, cal):
    global result

    if cal == K:
        result += 1
        return

    elif cal > K or k > N-1:
        return

    else:
        function(k+1, cal)
        function(k+1, cal+A[k])


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0

    function(0, 0)

    print('#{} {}'.format(t+1, result))