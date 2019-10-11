import sys
sys.stdin = open('5176_sample_input.txt', 'r')


def make_tree(left, point, right, k):
    if k == 0:
        return

    elif point-left == 1:
        child[point][0] = point-1

    elif point-left > 1:
        child[point][0] = (point-left)//2+1
        make_tree(left, (point-left)//2+1, point, k-1)

    if right-point == 1:
        child[point][1] = point+1

    elif right-point > 1:
        child[point][1] = point+(right-point)//2+1
        make_tree(point, point+(right-point)//2+1, right, k-1)


T = int(input())
for t in range(1):
    N = int(input())
    # print(N)

    child = [[0]*2 for _ in range(N+1)]
    # print(child)

    root = N//2 + 1
    print(root)

    make_tree(1, root, N, 2)
    print(child)