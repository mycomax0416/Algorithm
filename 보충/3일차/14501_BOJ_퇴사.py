import sys
sys.stdin = open('sample_14501.txt', 'r')

def backtrack(start, pay):
    global money
    global N

    if start >= len(Ti):
        money = max(money, pay)
        return

    if start + Ti[start] > len(Ti):
        money = max(money, pay)
        return

    else:
        backtrack(start + Ti[start], pay + Pi[start])
        backtrack(start + 1, pay) 


T = int(input())
for t in range(T):
    N = int(input())
    Ti = []
    Pi = []

    for n in range(N):
        t, p = map(int, input().split())
        Ti.append(t)
        Pi.append(p)

    money = 0
    result = []
    
    backtrack(0, 0)
    print(money)