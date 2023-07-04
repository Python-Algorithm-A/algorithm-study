import sys
input = sys.stdin.readline
n = int(input())
T=[0]
P=[0]
dp=[0] * (n+2)

for i in range(n):
    a, b = map(int,input().split())
    T.append(a)
    P.append(b)

#뒤->앞 으로 확인
for i in range(n,0,-1):
    if i+T[i]>(n+1): # 기한을 초과할 경우
        dp[i]=dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+T[i]]+P[i]) # 현재 날짜의 상담을 할 것인지 말것인지

print(dp[1])
