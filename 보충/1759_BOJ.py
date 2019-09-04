import sys
sys.stdin = open('BOJ_1759_input.txt', 'r')

def backtrack(k, start):
    global result
    global L

    if k >= L:
        result.append(choice[:])
        return

    else:
        for idx in range(start, len(alphabet)):
            choice[k] = alphabet[idx]
            backtrack(k+1, idx+1)    

L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()

choice = ['']*L
result = []
aeiou = 'aeiou'

backtrack(0, 0)

for test in result:
    vowel = []
    consonant = []
    output = ''

    for word in test:
        if word in aeiou:
            vowel.append(word)

        else:
            consonant.append(word)

    if len(vowel) >= 1 and len(consonant) >= 2:
        for idx in range(len(test)):
            output += test[idx]
    
    print(output)
