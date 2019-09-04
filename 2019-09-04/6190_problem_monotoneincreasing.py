import sys
sys.stdin = open('6190_sample_input.txt', 'r')

def backtrack(k, start):
    global result

    if k >= 2:
        chr = choice[:]
        result.append(chr[0]*chr[1])
        return

    else:
        for idx in range(start, len(arr)):
            choice[k] = arr[idx]
            backtrack(k+1, idx+1)


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    choice = ['']*2
    result = []
    ans = []

    backtrack(0, 0)
    print(result)
    result.sort()

    for test in result:
        num = str(test)
        sign = True

        for idx in range(len(num)-1):
            if num[idx] > num[idx+1]:
                sign = False

        if sign == True:
            ans.append(test)
    
    if ans == []:
        ans = -1

    print('#{} {}'.format(t+1, max(ans)))
