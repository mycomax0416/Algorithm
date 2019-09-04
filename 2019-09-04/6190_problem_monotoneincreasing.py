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
    ans = -1

    backtrack(0, 0)
    result.sort()

    while result:
        num = result.pop()
        num = str(num)
        sign = False

        for idx in range(len(num)-1):
            if num[0] != num[len(num)-1] and num[idx] < num[idx+1]:
                ans = num
                sign = True
                break
        
        if sign == True:
            break

    print('#{} {}'.format(t+1, ans))
