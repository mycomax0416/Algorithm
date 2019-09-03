import sys
sys.stdin = open('sample_14501.txt', 'r')

def work(N):
    if N < 0:
        return

    else:
        for i in range(2):
            if i == 0:
                def work(N-1)

            else:
                visit[0] = True
                result += arr[0]
                N -= arr[0][1]
                def work(N)

T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))
    print(arr)

    visit = [False for _ in range(N+1)]
    result = []

    def(N)



