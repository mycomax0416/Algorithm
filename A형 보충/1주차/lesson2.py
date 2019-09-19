# 순열/조합 생성 <--- 백트래킹 이해
# 순열/조합 생성하는 방법(과정) -> 재귀 호출로
#       --> 상태 공간 트리로 표현 --> 재귀 함수 호출 트리
#       --> 선택의 과정
# 재귀 함수 호출 트리
# 부분 집합을 생성
# 원소의 수 = N
# N번의 선택을 통해서 부분집합 생성. 각각의 원소에 대해서
# 매번 선택할 때의 선택지 ==> 2개
path = [0] * 3
def subset(k, n):
    if k == n:
        print(path)
        return
    # 함수 호출이 선택이다.
    path[k] = -1; subset(k+1, n)
    path[k] = 1; subset(k+1, n)

subset(0, 3)


# 순열 생성
# 모든 순열을 생성하는 과정을 선택의 과정
N = 3   # (0, 1, 2)
for i in range(N):
    for j in range(N):
        if i == j: continue
        for k in range(N):
            if k == i or k == j: continue
            print(i, j, k)


order = []
visit = [0] * 3
N = 3
def perm(k, n):
    if k == n:
        return

    for i in range(N):
        if visit[i]: continue
        visit[i] =1
        order.append(i)
        perm(k+1, n)
        order.pop()
        visit[i] = 0


# 조합 생성
arr = 'ABCDE'
N = 5       # {0, 1, 2, 3, 4}
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            print(arr[i], arr[j], arr[k])


N, R = 5, 3 # {0, 1, 2, 3, 4}
choose = []

def comb(k, s): # 선택할 요소의 시작값
    if k == R:  # 모두 선택
        print(choose)
        return

    for i in range(s, N):
        choose.append(i)
        comb(k+1, i+1)
        choose.pop()

comb(0, 0)