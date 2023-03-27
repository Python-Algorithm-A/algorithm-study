n=3
arr = [1, 3, 5]
su = sum(arr)//2

# 원소의 합이 홀수면 False
if sum(arr) % 2 !=0:
    print(False)

# dp 초기화
dp = [[0] * (n+1) for _ in range(su+1)]

for j in range(n+1):
    dp[0][j] = True
for i in range(1, su+1):
    dp[i][0] = False

# dp
for i in range(1, su+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] # 바로 왼쪽

        # 해당 원소가 포함되기 전에 해당 원소 값만큼 모자란 sum을 만들 수 있는지
        if i>=arr[j-1]:
            dp[i][j] |= dp[i-arr[j-1]][j-1]

print(dp[su][n])