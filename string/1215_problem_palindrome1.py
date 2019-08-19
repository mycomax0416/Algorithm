import sys
sys.stdin = open('1215_sample_input.txt', 'r')


for i in range(10):
    P_len = int(input())
    arr = []
    count = 0

    for j in range(8):
        arr += [input()]

    for y in range(8):
        for x in range(8-P_len+1):
            word = ''
            for p in range(P_len):
                word += arr[y][x+p]
            
            if word == word[::-1]:
                count += 1

    for x in range(8):
        for y in range(8-P_len+1):
            word = ''
            for p in range(P_len):
                word += arr[y+p][x]

            if word == word[::-1]:
                count += 1
    
    print('#{} {}'.format(i + 1, count))