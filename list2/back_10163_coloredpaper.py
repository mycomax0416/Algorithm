import sys
sys.stdin = open('back_10163_sample.txt', 'r')

N = int(input())
background_list = [[0] * 100 for a in range(100)]

for turn in range(N):

    arr = list(map(int, input().split()))
    turn_x = arr[0]
    turn_y = arr[1]
    width = arr[2]
    height = arr[3]

    for y in range(height):
        for x in range(width):
            background_list[turn_y+y][turn_x+x] = turn+1
    
for check in range(N):
    count = 0
    
    for back_y in range(100):
        for back_x in range(100):
            if background_list[back_y][back_x] == check+1:
                count += 1
    
    print(count)