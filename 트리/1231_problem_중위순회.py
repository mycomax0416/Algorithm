import sys
sys.stdin = open('1231_sample_input.txt', 'r')


def inorder(n):     # 중위 순회
    if n != 0:
        inorder(child[n][0])
        print(n, end=" ")
        inorder(child[n][1])


for t in range(1):
    N = int(input())

    child = [[0]*2 for _ in range(N+1)]
    alpha = [[''] for _ in range(N+1)]
    print(child)
    # print(alpha)

    for n in range(N):
        data = input().split()
        print(data)