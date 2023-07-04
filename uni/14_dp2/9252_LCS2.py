arr1 = list(input())
arr2 = list(input())
n = len(arr1)
m = len(arr2)
dp = [[0] * (m+1) for _ in range(n+1)]

#LCS 길이 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])

result = []
i = n
j = m

# dp 테이블을 거슬러 올라가면서 LCS 찾기
# 왼쪽과 위쪽의 숫자 모두 현재의 숫자와 다르면 대각선으로 올라가기
# 왼쪽의 숫자가 현재의 숫자와 같으면 왼쪽으로, 위쪽도 같은 방식
while i>=0 and j>=0:
    if dp[i][j] != dp[i-1][j] and dp[i][j] != dp[i][j-1]:
        result.append(arr1[i-1])
        i-=1
        j-=1
    elif dp[i-1][j] == dp[i][j]:
        i-=1
    elif dp[i][j-1] == dp[i][j]:
        j-=1

len_result=len(result)
if len_result>=1:
    for i in range(len_result-1, -1, -1):
        print(result[i], end='')
    print()



