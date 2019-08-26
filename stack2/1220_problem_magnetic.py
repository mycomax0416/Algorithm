import sys
sys.stdin = open('1220_sample_input.txt', 'r')

for i in range(10):
    j = int(input())

    arr = []
    count = 0
    
    for k in range(j):
        arr += [list(map(int, input().split()))]


    for x in range(100):
        column = []
        for y in range(100):
            if arr[y][x] != 0:
                column += [arr[y][x]]

        stack = []
        if len(column) > 0:
            stack += [column.pop()]

        while len(column) > 0:
            if column[-1] != stack[-1]:
                stack += [column.pop()]
            else:
                column.pop()
        
        if stack[-1] == 2:
            stack.pop()

        count += stack.count(2)

    print('#{} {}'.format(i+1, count))
