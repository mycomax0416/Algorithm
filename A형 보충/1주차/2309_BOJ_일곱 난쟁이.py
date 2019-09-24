import sys
sys.stdin = open('2309_BOJ_input.txt', 'r')


def pick(k, s):
    if k >= 2:
        combis.append(choose[:])
        return

    else:
        for idx in range(s, 9):
            choose.append(arr[idx])
            pick(k+1, idx+1)
            choose.pop()
            

arr = [int(input()) for _ in range(9)]

choose = []
combis = []

pick(0, 0)

for combi in combis:
    test = arr[:]

    for x in combi:
        test.remove(x)

    if sum(test) == 100:
        test.sort()

        for result in test:
            print(result)

        break