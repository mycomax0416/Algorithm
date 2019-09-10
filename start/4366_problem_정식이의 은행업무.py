import sys, copy
sys.stdin = open('4366_sample_input.txt', 'r')


def make_test_2(convert_2):
    list_convert_2 = list(convert_2)

    for idx in range(len(list_convert_2)):
        make_chr_2 = copy.deepcopy(list_convert_2)
        
        if list_convert_2[idx] == '1':
            make_chr_2[idx] = '0'
            test_group_2.append(''.join(make_chr_2))

        else:
            make_chr_2[idx] = '1'
            test_group_2.append(''.join(make_chr_2))

    return


def make_test_3(convert_3):
    list_convert_3 = list(convert_3)

    for idx in range(len(list_convert_3)):
        make_chr_3_1 = copy.deepcopy(list_convert_3)
        make_chr_3_2 = copy.deepcopy(list_convert_3)

        if list_convert_3[idx] == '2':
            make_chr_3_1[idx] = '1'
            test_group_3.append(''.join(make_chr_3_1))
            make_chr_3_2[idx] = '0'
            test_group_3.append(''.join(make_chr_3_2))

        elif list_convert_3[idx] == '1':
            make_chr_3_1[idx] = '2'
            test_group_3.append(''.join(make_chr_3_1))
            make_chr_3_2[idx] = '0'
            test_group_3.append(''.join(make_chr_3_2))

        else:
            make_chr_3_1[idx] = '2'
            test_group_3.append(''.join(make_chr_3_1))
            make_chr_3_2[idx] = '1'
            test_group_3.append(''.join(make_chr_3_2))

    return


T = int(input())
for t in range(T):
    print('#{}'.format(t+1), end=' ')

    tc_2 = str(input())
    tc_3 = str(input())

    test_group_2 = []
    make_test_2(tc_2)

    test_group_3 = []
    make_test_3(tc_3)

    for test_2 in test_group_2:
        for test_3 in test_group_3:
            if int(test_2, 2) == int(test_3, 3):
                print(int(test_2, 2))
                break
