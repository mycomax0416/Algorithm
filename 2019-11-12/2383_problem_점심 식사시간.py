import sys
sys.stdin = open('2383_sample_input.txt', 'r')


T = int(input())
for t in range(1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    stair_infos = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] != 1 and arr[y][x] != 0:
                stair_infos.append([x, y, arr[y][x], 3])
                                # x, y, 계단시간, 정원

    person_infos = []
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                person_info = []
                for stair_info in stair_infos:
                    stair_x, stair_y, time, max_count = stair_info
                    person_info.append(abs(x-stair_x)+abs(y-stair_y)+1+time)
                person_infos.append(person_info)

    print(sorted(person_infos, reverse=True))

    time = 0
    counts = [3 for _ in range(len(stair_infos))]
    delays = []

    time = 5
    # while person_infos:
    while time != 7:
        print(time)
        time += 1
        for i in range(4):
            do = True
            while do:
                will_remove = 0
                
                for person_info in sorted(person_infos, reverse=True):
                    for time_idx in range(len(person_info)):
                        if person_info[time_idx] == time:
                            if counts[time_idx] > 0:
                                counts[time_idx] -= 1
                                delays.append((time_idx, time+stair_infos[time_idx][2]))
                                will_remove = person_info
                                do = False
                                break

                    if do == False:
                        break

                if will_remove != 0:
                    person_infos.remove(will_remove)

                for count_idx in range(len(counts)):
                    if counts[count_idx] == 0:
                        for person_info in person_infos:
                            person_info[count_idx] += stair_infos[count_idx][2]
        
            for delay in delays:
                return_idx, return_time = delay
                if return_time == time:
                    counts[return_idx] += 1
                    for person_info in person_infos:
                        person_info[return_idx] -= stair_infos[return_idx][2]


        print(counts)
        print(person_infos)
        print(delays)