# 단순재귀
# def rodCut(n, p):
#     if n==0: # 종료조건
#             return 0
#     else:
#         r = -1
#         for i in range(1, n+1):
#             r = max(r, p[i] + rodCut(n-i,p))
#         return r

# def rodCut(n, p):
#     r = [0] * (n+1)
#     for i in range(1, n+1):
#         r[i] = -1
#         for j in range(1, i+1):
#             r[i] = max(r[i], r[i-j] + p[j])
#     return r[n]
#
# def rodCut(n, p):
#     if dp[n] < 0: # 계산을 하지 않았다면
#         if n == 0:
#             dp[n] = 0
#         else:
#             dp[n] = -1
#             for i in range(1, n+1):
#                 dp[n] = max(dp[n], p[i] + rodCut(n-i, p))
#     return dp[n]

def rodCut(n, p):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = -1
        for j in range(1, i+1):
            dp[i] = max(dp[i], dp[i-j] + p[j])
    return dp[n]

n = 4
p = [0, 1, 5, 8, 9]
dp = [-1] * (n+1)
print(rodCut(n, p))
