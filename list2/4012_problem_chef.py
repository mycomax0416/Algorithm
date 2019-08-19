import sys
sys.stdin = open('4012_sample.txt', 'r')

T = int(input())

for i in range(3):
    N = int(input())
   
    arr = []
    for j in range(N): 
        arr += [list(map(int, input().split()))]
    
    S_ij = arr[0][1] + arr[1][0]
    # for y in range(N):
    #     for x in range(y+1, N):

#-------------------

arr = [10, 20, 30, 40, 50, 60, 70, 80]
N = 4

for aa in range(1<<4):
    A, B = [], []
    for i in range(N):
        if aa & (1 << i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    
    if len(A) == len(B):
        print(A, B)