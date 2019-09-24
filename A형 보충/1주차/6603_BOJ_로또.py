import sys
sys.stdin = open('6603_BOJ_input.txt')


def pick(k, s):
    if k >= remove:
        combis.append(choose[:])
        return

    else:
        for idx in range(s, k):
            choose.append(S[idx])
            pick(k+1, idx+1)
            choose.pop()


get = True
while get:
    S = list(map(int, input().split()))
    
    if S == [0]:
        get = False
        break
    
    k = S.pop(0)
    S.sort()
    # print(k)
    # print(S)

    remove = k - 6
    print(remove)

    choose = []
    combis = []

    pick(0, 0)
    
    print(combis)