import sys
sys.stdin = open('5205_sample_input.txt', 'r')


def quickSort(lo, hi):
    if lo >= hi:
        return
    i = lo - 1
    for j in range(lo, hi):
        if A[hi] >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]

    i += 1
    A[hi], A[i] = A[i], A[hi]

    quickSort(lo, i - 1)
    quickSort(i + 1, hi)


T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    quickSort(0, len(A)-1)

    print('#{} {}'.format(t+1, A[N//2]))