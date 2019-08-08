import sys
sys.stdin = open('back_10815_sample.txt', 'r')

N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

result = [0] * M

for m in range(len(M_arr)):
    for n in N_arr:
        if M_arr[m] == n:
            result[m] += 1
 
print(' '.join(list(map(str, result))))

# input()
# n = set(map(int, input().split()))
# print(n)
# input()
# m = list(map(int, input().split()))
# for i in m:
#     if i in n:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')
