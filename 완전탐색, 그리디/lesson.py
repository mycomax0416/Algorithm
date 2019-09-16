# arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 10]

# def getMin(s, e):       # 최소값 구하기
#     if s == e:          # 기저 사례
#         return arr[s]
#     else:
#         mid = (s+e) // 2
#         l = getMin(s, mid)        # 매개변수 -> 문제의 크기, 반환값 -> 문제
#         r = getMin(mid+1, e)
#         return min(l, r)

# print(getMin(0, len(arr)-1))

# # 재귀 호출
# # 1. 동적계획법(DP) / 분할정복 => 재귀적 정의 구현할 때
# #                               - 부분문제간의 관계(큰문제와 작은문제간 관계)
# # 2. 탐색
# #   - 그래프 깊이 우선 탐색(DFS), 트리 순회
# #   - 백트래킹 --> 상태공간 트리, 그래프
# # --------------------------

# arr = [1, 2, 3, 4]
# N = len(arr)

# def perm(k):
#     if k == N:
#         print(arr)
    
#     else:
#         for i in range(k, N):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(k+1)
#             arr[k], arr[i] = arr[i], arr[k]

# perm(0)
#-----------------------------------

arr = 'ABCDE'
N, R = len(arr), 3
choose = []

def comb(k, s):
    if k == R:
        print(choose)
    
    else:
        for i in range(s, N):
            choose.append(arr[i])
            comb(k+1, i+1)
            choose.pop()

comb(0, 0)


# choose = []
# for i in range(N - 2):
#     choose.append(arr[i])
#     for j in range(i+1, N - 1):
#         choose.append(arr[j])
#         for k in range(j+1, N):
#             choose.append(arr[k])
#             print(choose)
#             choose.pop()
#         choose.pop()
#     choose.pop()
#             # print(arr[i], arr[j], arr[k])