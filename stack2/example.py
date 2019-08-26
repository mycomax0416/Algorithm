# import sys
# sys.stdin = open('example_input.txt', 'r')

# test = input().split()
# stack = []

# for chr in test:
#     if chr.isdigit():
#         print(chr, end=' ')
#     else:
#         stack += [chr]

# while len(stack) > 0:
#     print(stack.pop(), end=' ')

#----------------------------------------------------1

# def backtrack(a, k, input):
#     global MAXCANDIDATES
#     c = [0] * MAXCANDIDATES

#     if k == input:
#         process_solution(a, k)
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)


# def construct_candidates(a,k,input,c):
#     c[0]=True
#     c[1]=False
#     return 2

# def process_solution(a, k):
# #----------------------------
#     arr = []
#     for i in range(k+1):
#         if a[i]:
#             arr += [i]
#     if sum(arr) == 10:
#         print(arr)
# #------------------------- 이부분만 수정
    
#     # 원본
#     # print('(', end=' ')
#     # for i in range(k+1):
#     #     if a[i]:
#     #         print(i, end=' ')
#     # print(')')


# MAXCANDIDATES=100
# NMAX=100
# a=[0]*NMAX
# backtrack(a, 0, 10)

#------------------------------------------------2

def qsort(a, low, high):
    if low < high:
        pviot = partition(a, low, high)
        qsort(a, low, pviot-1)
        qsort(a, pviot+1, high)


def partition(a, pivot, high):
    i = pivot + 1
    j = high
    
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j

a = [54, 88, 77, 26, 93, 17, 49]
print('정렬 전: ', a)
qsort(a, 0, len(a)-1)
print('정렬 후: ', a)
