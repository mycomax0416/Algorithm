import sys
sys.stdin = open('5648_sample_input2.txt', 'r')  

def move(in_arr):
    out_arr = [[[] for _ in range(21)] for _ in range(21)]

    for y in range(21):
        for x in range(21):
            if in_arr[y][x]:
                if in_arr[y][x][0][0] == 0:    # 상
                    out_arr[y+1][x].append(in_arr[y][x][0])
                
                elif in_arr[y][x][0][0] == 1:  # 하
                    out_arr[y-1][x].append(in_arr[y][x][0])

                elif in_arr[y][x][0][0] == 2:  # 좌
                    out_arr[y][x-1].append(in_arr[y][x][0])

                elif in_arr[y][x][0][0] == 3:  # 우
                    out_arr[y][x+1].append(in_arr[y][x][0])

    return out_arr

# def print_board(arr):
#     for row in arr:
#         for item in row:
#             sys.stdout.write("{}\t".format(item))
#         print()    

def check(arr):
    energy = 0
    for y in range(len(arr[0])):
        for x in range(len(arr[0])):
            if len(arr[y][x]) > 1:
                for atom in arr[y][x]:
                    energy += atom[1]
            elif len(arr[y][x]) == 1:
                if arr[y][x][0][0] == 40 and arr[y][x][0][3] == 0:
                    arr[y][x][0] == []

                elif arr[y][x][0][0] == 0 and arr[y][x][0][3] == 1:
                    arr[y][x][0] == []

                elif arr[y][x][0][1] == 0 and arr[y][x][0][3] == 2:
                    arr[y][x][0] == []

                elif arr[y][x][0][1] == 40 and arr[y][x][0][3] == 3:
                    arr[y][x][0] == []

    return energy


T = int(input())
for t in range(1):
    N = int(input())
    arr = [[[] for _ in range(41)] for _ in range(41)]
    atoms = []
    energy = 0

    for n in range(N):
        atoms.append(list(map(int, input().split())))
    
    print(atoms)

    for atom in atoms:
        arr[(atom[0]+10)*2][(atom[1]+10)*2] = [[atom[2], atom[3]]]
    
    while arr != [[[] for _ in range(41)] for _ in range(41)]:
        arr = move(arr)
        print(arr)
        energy += check(arr)
        print(energy)
    # print(energy)
