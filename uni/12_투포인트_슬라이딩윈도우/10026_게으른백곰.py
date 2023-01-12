import sys
input = sys.stdin.readline

n, k = map(int,input().split()) # 양동이 갯수, 좌우로 떨어질 수 있는 거리

arr = [0 for i in range(1000000)] # 양동이 배열
max_x=0 # 가장 큰 좌표

for _ in range(n):
    g, x = map(int,input().split())
    arr[x] = g
    max_x = max(max_x, x)


value = sum(arr[:k*2]) # 0~k*2에 위치한 물의 무게의 합
max_value = value

for i in range(max_x-k*2+1): # 슬리이딩 윈도우
    value-=arr[i]
    value+=arr[i+k*2+1]

    if value > max_value: # 최대 물의 무게 구하기
        max_value = value

print(max_value)
