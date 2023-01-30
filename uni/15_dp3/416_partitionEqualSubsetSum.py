def findMin(a, n):
    half_sum = sum(a)//2

    dp = [[0 for i in range(half_sum + 1)] for j in range(n + 1)] # 총 합의 반 까지만 만들어줌

    # 첫 행 첫 열 초기화
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, half_sum + 1):
        dp[0][j] = False

    # dp
    for i in range(1, n + 1):
        for j in range(1, half_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]

    return dp[n][half_sum]

nums = list(map(int, input().split()))
#nums = [3, 7, 2, 4]
n = len(nums)
if sum(nums) % 2 != 0: # 원소의 총 합이 홀수이면 false
    print(False)
print(findMin(nums, n))
