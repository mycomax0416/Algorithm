import sys
sys.stdin = open('15686_BOJ_input.txt', 'r')
    

def backtrack(k, start):
    global M

    if k >= M:
        chick_m.append(chick_c[:])
        # chick_m.append(copy.copy(chick_c))
        return

    else:
        for idx in range(start, len(chick_p)):
            chick_c[k] = chick_p[idx]
            backtrack(k + 1, idx + 1)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))

    chick_p = []
    house_p = []

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                chick_p.append([x, y])

            elif arr[y][x] == 1:
                house_p.append([x, y])

    chick_c = [[] for _ in range(M)]
    chick_m = []

    backtrack(0, 0)

    total_distance = []

    for chick_g in chick_m:
        distance = []

        for house_t in house_p:
            d = N * 2 + 1

            for chick_t in chick_g:
                if abs(chick_t[0]-house_t[0]) + abs(chick_t[1]-house_t[1]) < d:
                    d = abs(chick_t[0]-house_t[0]) + abs(chick_t[1]-house_t[1])

            distance.append(d)

        total_distance.append(sum(distance))

    print(min(total_distance))


