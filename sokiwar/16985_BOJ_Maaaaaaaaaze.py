import sys
sys.stdin = open('16985_BOJ_input.txt', 'r')


empty = [[0]*5 for _ in range(5)]
print(empty)

def spin():
    change = empty[:]

    for y in range(5):
        for x in range(5):
            change[x][4-y] = cube[0][y][x]
    print(change)


T = int(input())
# for t in range(T):
cube = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
print(cube[0])
spin()