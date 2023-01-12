n ,k = map(int,input().split())
arr = list(map(int, input().split()))

end=0
sum=0
length=n+1
count=0 # 조건에 맞는 부분합을 구하지 못했을 경우를 대비

# 투 포인터
for start in range(n): # 시작점은 차례대 접근
    while sum<k and end<n: # 부분합이 k보다 크거나 작기 전까지 & end가 끝점을 넘지 않을 때까지 부분합을 구함
        sum+=arr[end]
        end+=1

    if sum >= k: # 부분합이 k보다 넘게되면
        length = min(length, end-start) # 그때까지의 길이의 최솟값 구하기
        count+=1
    sum-=arr[start]

if count==0: # 조건에 맞는 부분합을 구하지 못하는 경우
    print(0)
else:
    print(length)