import sys
sys.stdin = open('5110_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = ''
    
    for m in range(M-1):
        insert_arr = list(map(int, input().split()))

        for idx in range(len(arr)):
            if arr[idx] > insert_arr[0]:
                for _ in range(N):
                    arr.insert(idx, insert_arr.pop())
                break
        
        if insert_arr:
            for _ in range(N):
                arr.append(insert_arr.pop(0))

    if len(arr) >= 10:
        for _ in range(10):
            result += ' ' + str(arr.pop())
        
    else:
        for _ in range(len(arr)):
            result += ' ' + str(arr.pop())

    print('#{}{}'.format(t+1, result))



#-------------------------------------
# import sys
# sys.stdin = open('5110_sample_input.txt', 'r')

# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = ''

#     for m in range(M-1):
#         insert_arr = list(map(int, input().split()))

#         for idx, val in enumerate(arr):
#             if val > insert_arr[0]:
#                 for _ in range(N):
#                     arr.insert(idx, insert_arr.pop())
#                 break
        
#         if insert_arr:
#             for _ in range(N):
#                 arr.append(insert_arr.pop(0))

#     if len(arr) >= 10:
#         for _ in range(10):
#             result += ' ' + str(arr.pop())
        
#     else:
#         for _ in range(len(arr)):
#             result += ' ' + str(arr.pop())

#     print('#{}{}'.format(t+1, result))
#---------------------------------------
# import sys
# sys.stdin = open('5110_sample_input.txt', 'r')

# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     arr = []
#     result = ''

#     while M > 0:
#         M -= 1
#         insert_arr = list(map(int, input().split()))

#         for idx, val in enumerate(arr):
#             if val > insert_arr[0]:
#                 while insert_arr:
#                     arr.insert(idx, insert_arr.pop())
#                 break
        
#         if insert_arr:
#             while insert_arr:
#                 arr.append(insert_arr.pop(0))

#     if len(arr) >= 10:
#         for _ in range(10):
#             result += ' ' + str(arr.pop())
        
#     else:
#         for _ in range(len(arr)):
#             result += ' ' + str(arr.pop())

#     print('#{}{}'.format(t+1, result))
