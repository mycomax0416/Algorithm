# 퇴사

# 가장 단순한 접근 방법은 상담을 하는 모든 경우를 생성해서 조사하는 것이다

# 최적해는 상담할 수 있는 날들 중에 일부를 골라서 한다. 즉, 상담일들을 전체 집합이라고 했을 때, 부분집합 중에 하나가 최적해가 된다.

# 상담일들의 부분 집합을 생성해서 각 상담일의 상담기간이 겹치는 부분집합은 제외한다.

# 상담기간이 겹치지는 않는 부분집합에 포함된 상담일의 이익의 총합이 최대인 것을 찾는다.
def possible(s, e):
    if e > N + 1:
        return False
    for i in range(s, e):
        if visit[i]:
            return False
    return True


def setValue(s, e, )


N = int(input())
arr = [(0, 0)]
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

visit = [False] * (N + 1)
ans = 0
for set in range(1, 1 << (N+1)):
    psum = 0
    for i in range(1, N + 1):
        if (set & (1 << i)) == 0: continue
        e = i + arr[i][0]
        if not possible(i, e):
            setValue(1, N + 1, False); break
        setValue(i, e, True)

        psum += arr[i][1]
    ans = max(ans, psum)
print(ans)