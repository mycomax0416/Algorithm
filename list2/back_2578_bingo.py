import sys
sys.stdin = open('back_2578_sample.txt', 'r')


bingo_arr = []

for i in range(5):
    bingo_arr += [list(map(int, input().split()))]

numbers = []

for j in range(5):
    numbers += list(map(int, input().split()))

answer = [0] * 12
bingo_count = 0
count = 0

for number in range(len(numbers)):
    count += 1
    for y in range(len(bingo_arr)):
        for x in range(len(bingo_arr[y])):
            if numbers[number] == bingo_arr[y][x]:
                answer[x] += 1
                answer[y+5] += 1
                if x == y:
                    answer[10] += 1
                if x+y == 4:
                    answer[11] += 1

    for five in range(len(answer)):
        if answer[five] == 5:
            answer[five] = 0
            bingo_count += 1

    if bingo_count >= 3:
        break
    
print(count)
