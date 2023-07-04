# dp 예제 문제
import sys
input = sys.stdin.readline

stair = []

n = int(input())
dp=[0] * n

for _ in range(n):
    stair.append(int(input()))

if n==1:
    print(stair[0])
elif n==2:
    print(stair[0]+stair[1])
elif n==3:
    print(max(stair[0]+stair[2], stair[1]+stair[2]))
else:
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[-1])

