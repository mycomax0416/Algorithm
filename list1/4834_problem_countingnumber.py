import sys

sys.stdin = open('4834_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    N = input()
    arr = input()

    number = 0
    my_max = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for j in range(len(arr)):
        result[int(arr[j])] += 1
    # print(result)
    #
        for n in range(len(result)):
            if result[n] >= my_max:
                my_max = result[n]
                number = n

    print('#{} {} {}'.format(i+1, number, my_max))