import sys
sys.stdin = open('4839_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    info = list(map(int, input().split()))
    Pa = info[1]
    Pb = info[2]
    
    result = ''
    count = [0, 0]
    
    for j in range(len(count)):
        P = info[0]
        l = 1
        c = 0
        
        while c != info[j+1]:
            c = int((l+P)/2)
            if (info[j+1]-l) > (P-info[j+1]):
                l = c
            else:
                P = c
            count[j] += 1
    
    if count[0] < count[1]:
        result = 'A'
    elif count[1] < count[0]:
        result = 'B'
    else:
        result = '0'

    print('#{} {}'.format(i + 1, result))

#---------------------------------------------------------
# import sys
# sys.stdin = open('4839_sample_input.txt', 'r')

# T = int(input())

# for i in range(T):
#     info = list(map(int, input().split()))
#     Pa = info[1]
#     Pb = info[2]
    
#     result = ''
#     count_a = 0
#     count_b = 0
    
#     P = info[0]
#     l = 1
#     c = 0
#     while c != Pa:
#         c = int((l+P)/2)
#         if (Pa-l) > (P-Pa):
#             l = c
#         else:
#             P = c
#         count_a += 1
    
#     P = info[0]
#     l = 1
#     c = 0
#     while c != Pb:
#         c = int((l+P)/2)
#         if (Pb-l) > (P-Pb):
#             l = c
#         else:
#             P = c
#         count_b += 1

#     if count_a < count_b:
#         result = 'A'
#     elif count_b < count_a:
#         result = 'B'
#     else:
#         result = '0'

#     print('#{} {}'.format(i + 1, result))