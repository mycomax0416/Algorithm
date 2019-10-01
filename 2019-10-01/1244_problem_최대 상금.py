import sys
sys.stdin = open('1244_sample_input.txt', 'r')

T = int(input())
for t in range(T):
    num, count = map(int, input().split())
    tests = set([num])

    while count != 0:
        count -= 1
        new_tests = set()

        tests = list(tests)
        for _ in range(len(tests)):
            list_test = list(str(tests.pop(0)))

            for idx_1 in range(len(list_test)):
                for idx_2 in range(idx_1+1, len(list_test)):
                    trans_test = list_test[:]
                    trans_test[idx_1], trans_test[idx_2] = trans_test[idx_2], trans_test[idx_1]
                    new_tests.add(''.join(trans_test))
        
        tests = new_tests

    print('#{} {}'.format(t+1, max(tests)))