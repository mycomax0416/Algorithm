import sys
sys.stdin = open('4881_sample_input.txt', 'r')

MIN = 0
def perm(k, n, used, cursum):
    global MIN
    if cursum >= MIN: return

    if k == n:
        MIN = min(MIN, cursum)
        return

    for i in range(n):
        if used & (1 << i):  continue

        perm(k + 1, n, used | (1 << i), cursum + arr[k][i])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    MIN = 0xffffff
    perm(0, N, 0, 0)

    print("#%d %d" % (test_case, MIN))


#-----------------------------------
# T = int(input())

# for t in range(T):
#     N = int(input())
#     arr = []

#     for n in range(N):
#         arr += [list(map(int, input().split()))]

#     order = []
#     cnt = 1
    
#     def function(k, n, used):
#         if k == n:
#             global cnt
#             print(order)
#             cnt += 1
#             return

#         for i in range(n):
#             if used & (1<<i):
#                 continue
            
#             order += arr[k-1][i-1]
            
#             function(k+1, n, used | (1<<i))

#             order.pop()

#     function(0, len(arr), 0)
