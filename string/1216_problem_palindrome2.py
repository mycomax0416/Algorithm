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
    count = 0

    for j in range(100):
        arr += [input()]

    for i in range(100, 0, -1):
        print(i)
    
    start_P = 101
    result = 0
    mid_process = []

    while result == 0:
        start_P -= 1
        for y in range(100):
            for x in range(100-start_P+1):
                word = ''
                for p in range(start_P):
                    word += arr[y][x+p]

                if word == word[::-1]:
                    mid_process += [len(word)]
                break
    print(max(mid_process))





        
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