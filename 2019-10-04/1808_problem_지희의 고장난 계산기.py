import sys
sys.stdin = open('1808_sample_input.txt', 'r')


def cal(count, cal_num):
    global min_count

    if cal_num == X:
        min_count = min(min_count, count)
        return

    elif count >= min_count or cal_num >= X:
        return

    else:
        for num in select_nums:
            cal(count+1, cal_num*10+num)
            cal(count+2, cal_num*num)


T = int(input())
for t in range(3):
    arr = list(map(int, input().split()))
    X = int(input())

    select_nums = []
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for idx in range(10):
        if arr[idx] == 1:
            select_nums.append(nums[idx])

    print(select_nums)
    print(X)

    # min_count = -1

    min_count = 30
    cal(0, 0)

    print(min_count)
