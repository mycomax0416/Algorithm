import sys
sys.stdin = open('4865_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    str1 = input()
    str2 = list(input())
    dict_str2 = {}

    for key in str2:
        if key not in dict_str2:
            dict_str2[key] = 1
        else:
            dict_str2[key] += 1
    
    for key in dict_str2.keys():
        if key not in str1:
            dict_str2[key] = 0
  
    print('#{} {}'.format(i + 1, max(dict_str2.values())))