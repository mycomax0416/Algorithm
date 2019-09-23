N = 8
visit = [0] * N
cols = [0] * N      # 퀸의 열값을 저장
cnt = 0
def Possible(k, c): # k번 퀸의 열 1가 답이 되는 선택인지 조사
    for i in range(k):  # 0 ~ k-1 번 퀸과 대각선에 있는지 조사
        if k - i == abs(c - cols[i]):
            return False
    return True

def nQueen(k):
    if k == N:
        global cnt
        cnt += 1
    else:
        for i in range(N):
            if visit[i] or not Possible(k, i): continue
            visit[i] = 1
            cols[k] = i
            nQueen(k+1)
            visit[i] = 0

nQueen(0)
print(cnt)