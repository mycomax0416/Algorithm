import sys
sys.stdin = open('1259_sample_input.txt', 'r')

T = int(input())

for i in range(T):
    x = int(input())
    old_arr = list(map(int, input().split()))
   
    new_arr = []
    result = []

    for j in range(len(old_arr) // 2):
        new_arr.append([old_arr.pop(0), old_arr.pop(0)])
  
    standard = new_arr[0]
    result += [new_arr[0].copy()]

    while len(result) != x:
        for k in new_arr:

            if standard[1] == k[0]:
                standard[1] = k[1]
                result += [k]

            if k[1] == standard[0]:
                standard[0] = k[0]
                result.insert(0, k)

    mid_process = []

    for a in range(len(result)):
        mid_process += [result[a][0]] + [result[a][1]]

    final = list(map(str, mid_process))

    print('#{} {}'.format(i + 1, ' '.join(final)))