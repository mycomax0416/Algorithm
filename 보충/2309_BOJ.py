import sys
sys.stdin = open('BOJ_2309_input.txt', 'r')

arr = []
for n in range(9):
    arr += [int(input())]

for i in range(1 << 9):
    test = []

    for j in range(9):
        if i & (1<<j):
            test += [arr[j]]
            
    if len(test) == 7 and sum(test) == 100:
        test.sort()
        break

for result in test:
    print(result)
