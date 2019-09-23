# 순열 생성
arr = 'ABC'
N = len(arr)
order = [0] * N         # 순서를 저장
def perm(a, k, n):
    if k == n:
        print(a)
        # for idx in a:
        #     print(arr[idx], end='')
        # process_solution()
    else:
        visit = [False] * n
        for i in range(k):
            visit[a[i]] = True
        for i in range(n):
            if visit[i]: continue
            a[k] = i
            perm(a, k+1, n)


perm(order, 0, N)