import sys
sys.stdin = open('4047_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    state = True
    S, D, H, C = 13, 13, 13, 13

    cards = list(input())
    
    for _ in range(len(cards)//3):
        card = str(cards.pop(0) + cards.pop(0) + cards.pop(0))
        cards += [card]

    compare_dict = {}

    for card in cards:
        if card not in compare_dict:
            compare_dict[card] = 1
        elif card in compare_dict:
            compare_dict[card] += 1
    
    for key in compare_dict:
        if compare_dict[key] > 1:
            state = False
            print('#{} ERROR'.format(t+1))
            break
        
        if key[0] == 'S':
            S -= 1

        elif key[0] == 'D':
            D -= 1
        
        elif key[0] == 'H':
            H -= 1
        
        elif key[0] == 'C':
            C -= 1

    if state:
        print('#{} {} {} {} {}'.format(t+1, S, D, H, C))
#----------------------------------------------------
# import sys
# sys.stdin = open('4047_sample_input.txt', 'r')

# T = int(input())
# for t in range(T):
#     state = True
    
#     standard_dict = {}
#     patterns = ['S', 'D', 'H', 'C']
#     nums = [num+1 for num in range(13)]

#     for pattern in patterns:
#         standard_dict[pattern] = []
#         for num in nums:
#             standard_dict[pattern] += [num]
    
#     cards = list(input())

#     if len(cards) % 3 != 0:
#         state = False
#         print('#{} ERROR'.format(t+1))
    
#     for _ in range(len(cards)//3):
#         card = str(cards.pop(0) + cards.pop(0) + cards.pop(0))
#         cards += [card]

#     compare_dict = {}

#     for card in cards:
#         if card not in compare_dict:
#             compare_dict[card] = 1
#         elif card in compare_dict:
#             compare_dict[card] += 1

#     for key in compare_dict:
#         if compare_dict[key] > 1:
#             state = False
#             print('#{} ERROR'.format(t+1))

#     if state:
#         for card in compare_dict:
#             T = card[0]
#             XY = int(card[1:])
#             standard_dict[T].pop(XY-1)
    
#         print('#{} {} {} {} {}'.format(t+1, len(standard_dict['S']), len(standard_dict['D']), len(standard_dict['H']), len(standard_dict['C'])))
