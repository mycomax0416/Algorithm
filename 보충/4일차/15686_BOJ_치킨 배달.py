import sys
sys.stdin = open('15686_BOJ_input.txt', 'r')
    
def backtrack(k, start):
    global M
    if k >= M:
        house_m.append(house_c[:])
        return
    
    else:
        for idx in range(start, M):
            house_c[k] = house_p[idx]
            backtrack(k+1, idx+1)



T = int(input())
for t in range(1):
    N, M = map(int, input().split())
    # print(N, M)

    arr = []
    for n in range(N):
        arr.append(list(map(int, input().split())))
    # print(arr)

    chick_p = []
    house_p = []

    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                chick_p.append([x, y])

            elif arr[y][x] == 1:
                house_p.append([x, y])
    # print(chick_p)
    # print(house_p)

    house_c = [''] * M
    house_m = []

    backtrack(0, 0)

    # print(house_m)

    all_chick_len = []

    for house_t in house_m:
        chick_len = 2 * N + 1
        # print(house_t[0])
        # print(chick_len)

        for chick_t in chick_p:
            if abs(house_t[0]-chick_t[0]) + abs(house_t[1]-chick_t[1]) < chick_len:
                chick_len = abs(house_t[0]-chick_t[0]) + abs(house_t[1]-chick_t[1])

        all_chick_len.append(chick_len)
    
    # print(all_chick_len)

    print(sum(all_chick_len))


