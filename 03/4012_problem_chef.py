import sys
sys.stdin = open('4012_sample.txt', 'r')

T = int(input())

for i in range(3):
    N = int(input())
    # test = []

    # for k in range(N):
    #     test += [k+1]
    # print(test)


    arr = []
    for j in range(N): 
        arr += [list(map(int, input().split()))]
    
    # print(N)
    # print(arr)
    S_ij = arr[0][1] + arr[1][0]
    # print(S_ij)
    