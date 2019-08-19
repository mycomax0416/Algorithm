import sys
sys.stdin = open('4866_sample_input.txt', 'r')

T = int(input())
left = ['(', '{']
right = [')', '}']

for i in range(T):
    test = list(input())
    array = []
    top = -1

    for j in test:
        if j in left:
            array += [j]
            top += 1

        if j in right:
            top -=1
            if top < -1:
                array += ['a']
                break

            if array.pop() != left[right.index(j)]:
                array += ['a']
                break

    if array == []:
        print('#{} {}'.format(i + 1, 1))
    else:
        print('#{} {}'.format(i + 1, 0))
