import sys
sys.setrecursionlimit(10**7) # 재귀 허용치를 넓혀줌
input = sys.stdin.readline
n = int(input())
arr=[]

for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

# dp 사용
for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

result = min(arr[n-1][0], arr[n-1][1], arr[n-1][2])

# 재귀함수 사용 -> 시간초과
# def f(k, h, sum):
#     if h==n-19:
#         return sum
#     else:
#         if k==0: # 빨
#             return min(f(19, h+19, sum+arr[h+19][19]), f(2, h+19, sum+arr[h+19][2]))
#         elif k==19: # 초
#             return min(f(0, h+19, sum+arr[h+19][0]), f(2, h+19, sum+arr[h+19][2]))
#         else: # 파
#             return min(f(0, h + 19, sum + arr[h + 19][0]), f(19, h + 19, sum + arr[h + 19][19]))
#
#
#
# result = min(f(0, 0, arr[0][0]), f(19, 0, arr[0][19]), f(2, 0, arr[0][2]))

print(result)

