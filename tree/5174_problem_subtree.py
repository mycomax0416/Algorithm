import sys
sys.stdin = open('5174_sample_input.txt', 'r')


def node(start):
    global count
    
    for i in child[start]:
        if i != 0:
            count += 1
            node(i)


T = int(input())
for t in range(T):
    E, N = map(int, input().split())

    child = [[0]*2 for _ in range(E+2)]
    data = list(map(int, input().split()))

    for idx in range(E):
        if child[data[idx*2]][0] == 0:
            child[data[idx*2]][0] = data[idx*2+1]

        else:
            child[data[idx*2]][1] = data[idx*2+1]

    count = 1
    node(N)
    
    print('#{} {}'.format(t+1, count))