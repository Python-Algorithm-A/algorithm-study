seq = [2, 3, -6, 1, 3, -1, 2, 4]
n = len(seq)

# a = [1, -1, 1, -1, 1, ...]
a=[]
k=1
for i in range(n):
    num = seq[i]*k
    a.append(num)
    k*=-1

# b = [-1, 1, -1, 1, -1, ...]
b=[]
k=-1
for i in range(n):
    num = seq[i]*k
    b.append(num)
    k*=-1

# dp를 사용하여 연속 부분수열의 최대합 구하기
# dp[i]의 값은 i번째의 원소를 마지막으로 했을 때의 부분 수열의 최대값
result=0
dp = [None] * len(a)
dp[0] = a[0]
for i in range(1, len(a)):
    dp[i] = max(0, dp[i-1]) + a[i]
result = max(dp)

dp = [None] * len(b)
dp[0] = b[0]
for i in range(1, len(b)):
    dp[i] = max(0, dp[i-1]) + b[i]
result = max(result, max(dp))

print(result)