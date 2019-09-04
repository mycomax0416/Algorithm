import sys
sys.stdin = open('14888_BOJ_input.txt', 'r')

def backtrack(pl, mi, mu, di, k, cal):
    global nums

    if len(nums) == k:
        result.append(cal)
        return

    if pl > 0:
        cal += nums[k]
        backtrack(pl-1, mi, mu, di, k+1, cal)

    if mi > 0:
        cal -= nums[k]
        backtrack(pl, mi-1, mu, di, k+1, cal)

    if mu > 0:
        cal *= nums[k]
        backtrack(pl, mi, mu-1, di, k+1, cal)

    if di > 0:
        # if nums[k] < 0:
        #     cal //= (-nums[k])
        #     cal = -cal
        #
        # else:
        #     cal //= nums[k]
        cal //= nums[k]

        backtrack(pl, mi, mu, di-1, k+1, cal)

T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    pl, mi, mu, di = map(int, input().split())
    result = []

    cal = nums.pop(0)

    backtrack(pl, mi, mu, di, 0, cal)

    print(min(result))
    print(max(result))
    print('-----')

