import sys
sys.stdin = open('input.txt', 'r')
# pay = 0
#
# def swim(arr):
#     global pay
#     print(arr)
#     if arr == [0 for _ in range(12)]:
#         print(pay)
#         return
#
#     else:
#         for idx in range(len(arr)):
#             if arr[idx] != 0:
#                 for no in range(3):
#                     if no == 0:
#                         pay += arr[idx] * day
#                         arr[idx] = 0
#                         swim(arr)
#
#                     elif no == 1:
#                         pay += one
#                         arr[idx] = 0
#                         swim(arr)
#
#                     else:
#                         if idx+2 == len(arr) + 1:
#                             pay += three
#                             arr[idx] = 0
#                             swim(arr)
#
#                         elif idx+2 == len(arr):
#                             pay += three
#                             arr[idx], arr[idx+1] = 0, 0
#                             swim(arr)
#
#                         elif idx+2 < len(arr):
#                             arr[idx], arr[idx+1], arr[idx+2] = 0, 0, 0
#                             pay += three
#                             swim(arr)
# T = int(input())
# for t in range(1):
#     day, one, three, year = map(int, input().split())
#     print(day, one, three, year)
#     use = list(map(int, input().split()))
#     print(use)
#     pay = 0
#     swim(use)
#---------------------------------

def backtrack(n, cost): # n: 현재 달, cost: 이용료
    global ans
    if n >= 13:
        ans = min(ans, cost)
        return
    # 이용일이 없는 경우
    if arr[n] == 0:
        backtrack(n+1, cost)
    # 이용일이 있는 경우
    else:
        # 3가지 선택지
        backtrack(n + 1, cost + day * arr[n])
        backtrack(n + 1, cost + month)
        backtrack(n + 3, cost + quarter)



T = int(input())
for tc in range(1, T + 1):
    day, month, quarter, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    ans = year

    backtrack(1, 0)
    print(ans)