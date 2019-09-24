import sys
sys.stdin = open('3980_BOJ_input.txt', 'r')


def test(k, cal):
    global max_position

    if k >= 11:
        max_position = max(max_position, cal)
        return

    else:
        for x in range(11):
            if S[k][x] != 0 and check[x] == False:
                check[x] = True

                test(k+1, cal+S[k][x])

                check[x] = False

        return


C = int(input())
for c in range(C):
    S = [list(map(int, input().split())) for _ in range(11)]

    max_position = 0
    check = [False for _ in range(11)]

    test(0, 0)

    print(max_position)