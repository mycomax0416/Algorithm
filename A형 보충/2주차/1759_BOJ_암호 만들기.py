import sys
sys.stdin = open('1759_BOJ_input.txt', 'r')

vowel = ['a', 'e', 'i', 'o', 'u']

def backtrack(k, start):
    if k >= L:
        vowel_count = 0
        consonant_count = 0

        for word in choice:
            if word in vowel:
                vowel_count += 1
            else:
                consonant_count += 1

        if vowel_count >= 1 and consonant_count >= 2:
            result = ''.join(choice)
            print(result)
        
        return

    else:
        for idx in range(start, C):
            choice.append(arr[idx])

            backtrack(k+1, idx+1)

            choice.pop()


L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()

choice = []

backtrack(0, 0)