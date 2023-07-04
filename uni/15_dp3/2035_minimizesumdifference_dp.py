nums=[2,-1,0,4,-2,-9]
#nums = [3, 7, 2, 7]
nums.sort()
print(nums)

min_sum=0
max_sum=0
n = len(nums)

arr_sum=[]
if not all(nums):
    min_sum = sum(i for i in nums if i<0)
    max_sum = sum(i for i in nums if i>=0)
    arr_abs_sum = abs(max_sum-min_sum)

    for data in range(min_sum, max_sum + 1):
        arr_sum.append(data)
else:
    arr_abs_sum = sum(nums)
    for data in range(arr_abs_sum+1):
        arr_sum.append(data)

print(arr_sum)
print(arr_abs_sum)


n = len(nums)
dp = [[False] * (n+1) for _ in range(arr_abs_sum+1)]

index=0

# 첫 행열 초기화
if not all(nums): # 배열에 음수가 있을 때
    dp[0][0] = False
    for j in range(1, n+1):
        if nums[j-1]<0:
            dp[0][j]=False
            index=j
        else:
            dp[0][index] = True
            dp[0][j] = True

    for i in range(1, arr_abs_sum+1):
        if arr_sum[i]==0:
            dp[i][0] = True
        else:
            False

else: # 배열에 음수가 없을
    for j in range(0, n+1):
        dp[0][j] = True
    for i in range(1, arr_abs_sum+1):
        dp[i][0] = False



for i in range(1, arr_abs_sum+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1]

        if i >=nums[j-1] and (i-nums[j-1])<=18:

            dp[i][j] |= dp[i-nums[j-1]][j-1]

for x in range(arr_abs_sum+1):
    print(dp[x])



