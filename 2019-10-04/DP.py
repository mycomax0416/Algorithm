# def fibo(n):
#     global cnt
#     cnt += 1

#     if n < 2:
#         return n
    
#     else:
#         return fibo(n-1) + fibo(n-2)

# cnt = 0
# N = int(input())
# print('피보나치 결과:', fibo(N))
# print('호출횟수:', cnt)

# def fibo(n):    # DP를 이용한 피보나치(메모이제이션)
#     global cnt
#     cnt += 1

#     if n >= 2 and memo[n] == -1:
#         memo[n] = fibo(n-1) + fibo(n-2)
#     return memo[n]
    
# cnt = 0
# N = int(input())
# memo = [-1] * (N+1)
# memo[0] = 0
# memo[1] = 1

# print('피보나치 결과:', fibo(N))
# print(memo)
# print('호출횟수:', cnt)

def fibo(n):    # DP를 이용한 피보나치(반복)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

N = int(input())
memo = [-1] * (N+1)
print('피보나치 결과:', fibo(N))
print(memo)