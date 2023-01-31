import bisect
n = int(input())

arr=[]
dp=[]
for _ in range(n):
    arr.append(int(input()))

dp.append(arr[0])

#LIS 길이 찾기
for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        index = bisect.bisect_left(dp, arr[i])
        dp[index] = arr[i]

# 전체 길이 - LIS 길이
print(n-len(dp))
