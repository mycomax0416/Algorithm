import sys
sys.stdin = open('3234_sample_input.txt', 'r')


def function(k, left, right):
    global count

    if k >= N:
        if left >= right:
            count += 1
        return

    elif k == 0 or left >= right:
        for idx in range(N):
            if check[idx] == False:
                check[idx] = True

                function(k+1, left+arr[idx], right)
                function(k+1, left, right+arr[idx])

                check[idx] = False


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    check = [False for _ in range(N)]
    count = 0

    function(0, 0, 0)

    print('#{} {}'.format(t+1, count))