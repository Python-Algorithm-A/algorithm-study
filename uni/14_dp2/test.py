arr1 = list(input())
arr2 = list(input())
n = len(arr1)
m = len(arr2)
dp = [[0] * (m+1) for _ in range(n+1)]
print(dp)

k = 0
for i in range(n+1):
    for j in range(m+1):
        print(i, j)
        dp[i][j] = k
        k += 1

print(dp)