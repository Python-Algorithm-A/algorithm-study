import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp1=[0] * n
dp2=[0] * n

dp1[0] = arr[0] # 특정원소를 제거하지 않은 경우
dp2[0] =  0# 특정원소를 제거한 경우 (배열 모두가 음수인 경우에는 다른걸 넣어줘야 함)

for i in range(1, n):
    # 앞의 원소들과 현재의 원소를 합친 것과 현재의 원소 중 큰 것을 선택
    dp1[i] = max(dp1[i-1]+arr[i], arr[i])
    # 앞의 원소들 중 어떤 한 원소가 빠진 것에서 현재의 원소를 합친 것과 현재의 원소를 빼는 것 중 큰 것을 선택
    #  = 현재의 원소를 뺄지 아니면 앞의 원소들 중 하나를 뺄지
    dp2[i] = max(dp2[i - 1] + arr[i], dp1[i - 1])
print(max(max(dp1), max(dp2)))

# 시간초과
# minus=[]
# for i in range(n):
#     if arr[i]<0:
#         minus.append(i)
#
# result=0
# dp=[]
# for data in minus:
#     su=0
#     for i in range(n):
#         if i==data:
#             dp.append(su)
#         else:
#             if su<0:
#                 dp.append(arr[i])
#                 su=arr[i]
#             else:
#                 su += arr[i]
#                 dp.append(su)
#     su = max(dp)
#     result = max(result, su)
#     dp.clear()
# print(result)