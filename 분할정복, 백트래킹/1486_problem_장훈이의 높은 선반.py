import sys
sys.stdin = open('1486_sample_input.txt', 'r')


def backtrack():
    if B <= sum(choice) < min_height:
        min_height = sum(choice)
        return

    else:
        





T = int(input())
for t in range(1):
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))
    print(N, B)
    print(Hi)
    Hi.sort()
    print(Hi)

    min_height = 0
    for i in Hi:
        min_height += i

        if min_height >= B:
            break

    print(min_height)

    choice = []
    backtrack()