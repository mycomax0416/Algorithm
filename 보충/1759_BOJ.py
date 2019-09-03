import sys
sys.stdin = open('BOJ_1759_input.txt', 'r')

L, C = map(int, input().split())
# print(L, C)
alphabet = list(map(str, input().split()))

aeiou = 'aeiou'
consonant = []   # 자음
vowel = []   # 모음
# print(alphabet)

for x in alphabet:
    if x in aeiou:
        vowel.append(x)
    else:
        consonant.append(x)

print(vowel)
print(consonant)
