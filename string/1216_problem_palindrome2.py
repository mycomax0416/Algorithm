# import sys
# sys.stdin = open('1216_sample_input.txt', 'r')

# for i in range(10):
#     test_num = int(input())
#     arr = []
#     count = 0

#     for j in range(100):
#         arr += [input()]

#     P_len = 100
#     max_word_len = 1

#     for y in range(100):
#         for k in range(2, P_len):
#             for x in range(100-k+1):
#                 word = ''
#                 for p in range(k):
#                     word += arr[y][x+p]

#                 if word == word[::-1]:
#                     if len(word) > max_word_len:
#                         max_word_len = len(word)
        
#     for x in range(100):
#         for k in range(2, P_len):
#             for y in range(100-k+1):
#                 word = ''
#                 for p in range(k):
#                     word += arr[y+p][x]

#                 if word == word[::-1]:
#                     if len(word) > max_word_len:
#                         max_word_len = len(word)
    
#     print('#{} {}'.format(i + 1, max_word_len))

#--------------------------------

import sys
sys.stdin = open('1216_sample_input.txt', 'r')

for i in range(10):
    test_num = int(input())
    arr = []
    answer = 0

    for j in range(100):
        arr += [input()]
    # print(arr)
    for length in range(100, 1, -1):
        # print(length)

        for y in range(100):
            for x_case in range(100 - length + 1):
                # print(x_case)
                word = ''
                for x in range(length):
                    word += arr[y][x + x_case]
                # print(word)

                if word == word[::-1]:
                    answer += length
                    print(answer)
                    break
        
        if answer != 0:
                break

        for x in range(100):
            for y_case in range(100 - length + 1):
                # print(x_case)
                word = ''
                for y in range(length):
                    word += arr[y + y_case][x]
                # print(word)

                if word == word[::-1]:
                    answer += length
                    print(answer)
                    break
        
        if answer != 0:
                break

