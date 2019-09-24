import sys
sys.stdin = open('14501_BOJ_input.txt', 'r')

def backtrack(start, pay):
    global money

    if start == N:
        money = max(money, pay)
        return

    else:
        if start + Ti[start] <= N:
            backtrack(start+Ti[start], pay+Pi[start])
            
        backtrack(start+1, pay)


T = int(input())
for t in range(T):
    Ti = []
    Pi = []
    N = int(input())

    for _ in range(N):
        t, p = map(int, input().split())
        Ti.append(t)
        Pi.append(p)

    money = 0

    backtrack(0, 0)

    print(money)
