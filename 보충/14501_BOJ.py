import sys
sys.stdin = open('sample_14501.txt', 'r')

def backtrack(start, end, term, pay):
    global money
    if start >= end:
        pay = max(money, pay)
        return

    else:
        backtrack(start + term, end, Ti[start], pay + Pi[start])
        backtrack(start + 1, end, Ti[start+1], pay)

T = int(input())
for t in range(T):
    N = int(input())
    Ti = []
    Pi = []

    for n in range(N):
        t, p = map(int, input().split())
        Ti.append(t)
        Pi.append(p)
    # print(Ti)
    # print(Pi)
    money = 0
    
    backtrack(0, N, Ti[0], 0)

    print(money)