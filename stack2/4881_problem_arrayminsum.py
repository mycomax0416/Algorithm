import sys
sys.stdin = open('4881_sample_input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    arr = []

    for n in range(N):
        arr += [list(map(int, input().split()))]

    order = []
    cnt = 1
    
    def function(k, n, used):
        if k == n:
            global cnt
            print(order)
            cnt += 1
            return

        for i in range(n):
            if used & (1<<i):
                continue
            
            order += [arr[k-1][i-1]]
            
            function(k+1, n, used | (1<<i))

            order.pop()

    function(0, len(arr), 0)
