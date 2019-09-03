# 조합 생성
arr = 'ABCDE'
N = len(arr)    # N = 5
R = 3
choice = [''] * R

def backtrack(k, start):
    if k == R:
        print(choice)

    else:
        for i in range(start, N):
            choice[k] = arr[i]
            backtrack(k+1, i+1)

backtrack(0, 0)

# for i in range(N-2):    # N-2 대신 N 으로 해도 가능
#     for j in range(i+1, N-1):   # N-1 대신 N 으로 해도 가능
#         for k in range(j+1, N):
#             print(arr[i], arr[j], arr[k])

# 암호만들기 문제 BOJ 1759
# N 퀸 문제
# 대각선 판별
# if abs(r1 - r2) == abs(c1 - c2):
# 숨바꼭질 (BFS)
