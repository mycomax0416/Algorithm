import sys
sys.stdin = open('1231_sample_input.txt', 'r')


def inorder(n):     # 중위 순회
    global result

    if n != 0:
        inorder(child[n][0])
        result.append(word[n])
        inorder(child[n][1])


for t in range(10):
    N = int(input())
    result = []

    child = [[0]*2 for _ in range(N+1)]
    word = [[''] for _ in range(N+1)]

    for n in range(N):
        data = input().split()
        word[int(data[0])] = data[1]

        if len(data) > 2:
            child[int(data[0])][0] = int(data[2])

            if len(data) == 4:
                child[int(data[0])][1] = int(data[3])

    inorder(1)

    print('#{} {}'.format(t+1, ''.join(result)))