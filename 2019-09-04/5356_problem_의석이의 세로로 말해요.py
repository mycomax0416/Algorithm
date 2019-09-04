import sys
sys.stdin = open('5356_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    arr = []
    for _ in range(5):
        arr.append(input())

    length_long = len(arr[0])
    for length in arr:
        if len(length) > length_long:
            length_long = len(length)

    visit = [[False] * length_long for _ in range(5)]
    result = ''

    for y in range(5):
        for x in range(len(arr[y])):
            if arr[y][x]:
                visit[y][x] = True

    for x in range(length_long):
        for y in range(5):
            if visit[y][x]:
                result += arr[y][x]
    
    print('#{} {}'.format(t+1, result))
