def backtrack(pl, mi, mu, di, k, cal):
    global nums

    if len(nums) == k:
        result.append(cal)
        return

    if pl > 0:
        # cal += nums[k] <---- cal 값이변경되서 뒤쪽에 영향을 줌.
        backtrack(pl-1, mi, mu, di, k+1, cal + nums[k])

    if mi > 0:
        backtrack(pl, mi-1, mu, di, k+1, cal - nums[k])

    if mu > 0:
        backtrack(pl, mi, mu-1, di, k+1, cal * nums[k])

    if di > 0:
        tmp = 0
        if cal < 0:
            tmp = -((-cal)//nums[k])
        else:
            tmp = cal // nums[k]

        backtrack(pl, mi, mu, di-1, k+1, tmp)

N = int(input())
nums = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())
result = []

cal = nums.pop(0)

backtrack(pl, mi, mu, di, 0, cal)

print(max(result))
print(min(result))


