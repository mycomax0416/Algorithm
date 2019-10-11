import sys
sys.stdin = open('sample_lesson_input.txt', 'r')


def preorder(n):    # 전위 순회
    if n != 0:
        print(n, end=" ")
        preorder(child[n][0])
        preorder(child[n][1])


def inorder(n):     # 중위 순회
    if n != 0:
        inorder(child[n][0])
        print(n, end=" ")
        inorder(child[n][1])


def postorder(n):   # 후위 순회
    if n != 0:
        postorder(child[n][0])
        postorder(child[n][1])
        print(n, end=" ")


N = int(input())
arr = list(map(int, input().split()))
child = [[0]*2 for _ in range(N+1)]

for i in range(N-1):
    if child[arr[i*2]][0] == 0:     # 부모 노드 i*2에 자식 노드가 없는 경우
        child[arr[i*2]][0] = arr[i*2+1]

    else:       # 이미 자식이 한 개 있는 경우
        child[arr[i*2]][1] = arr[i*2+1]
print(child)
# print(child)
# print("전위 순회 결과: ", end=" ")
# preorder(1)
# print()
# print(child)

# print("중위 순회 결과: ", end=" ")
# inorder(1)
# print()

# print("후위 순회 결과: ", end=" ")
# postorder(1)
# print()