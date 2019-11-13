import sys
sys.stdin = open('4008_sample_input.txt', 'r')
from itertools import permutations


# def make_perm(k):
#     if k == len(formulas):
#         formulas_permutations.add(formulas_permutaion)

#     else:
#         for idx in range(len(formulas)):
#             if visit[idx] == False:
#                 visit[idx] = True
#                 formulas_permutaion.append(formulas[idx])

#                 make_perm(k+1)

#                 visit[idx] = False
#                 formulas_permutaion.pop()


T = int(input())
for t in range(1):
    N = int(input())
    formula_counts = list(map(int, input().split()))  # [+, -, *, /]
    numbers = list(map(int, input().split()))

    formulas = []
    for formula_idx in range(len(formula_counts)):
        for count in range(formula_counts[formula_idx]):
            if formula_idx == 0:
                formulas.append('+')
            elif formula_idx == 1:
                formulas.append('-')
            elif formula_idx == 2:
                formulas.append('*')
            else:
                formulas.append('/')

    # formulas_permutaion = []
    # visit = [False for _ in range(len(formulas))]
    # formulas_permutations = set()

    # make_perm(0)

    # print(formulas_permutations)
    #--------------
    formulas_permutations = set(permutations(formulas))
    print(formulas_permutations)

    # results = []
    # for formulas_permutation in formulas_permutations:
    #     result = numbers[0]
    #     for idx in range(len(formulas_permutation)):
    #         if formulas_permutation[idx] == '+':
    #             result += numbers[idx+1]
    #         elif formulas_permutation[idx] == '-':
    #             result -= numbers[idx+1]
    #         elif formulas_permutation[idx] == '*':
    #             result *= numbers[idx+1]
    #         else:
    #             result //= numbers[idx+1]
    #             # if result == -1:
    #             #     result += 1
    #     results.append(result)

    # max_result = max(results)
    # min_result = min(results)

    # print('#{} {}'.format(t+1, max_result-min_result))
