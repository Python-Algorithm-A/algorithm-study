arr = list(map(int, input()))
length = len(arr)

dp = [1] * length # dp를 1로 초기화
result=1
impossible=False # 암호해석 할 수 없는 경우 대비

if length == 0 or arr[0]==0: # 길이가 0 이거나 첫번째부터 0이 나오면 암호 해석 불가
    impossible = True
    print(0)

else:
    for i in range(1, length):
        if (arr[i-1]==0 or arr[i-1]>=3) and arr[i]==0: # 00, 30, 40, 50 ,... 인 경우 암호 해석 불가
            impossible=True
            print(0)
            break

        if arr[i-1]>=3 or (arr[i-1]==2 and arr[i]>=7): # 현재 숫자 단독  해석 할 수 없는 경우만
            dp[i]=result
        else:
            if arr[i]==0: # 0이 나온 경우
                result = dp[i-2]
                dp[i]=dp[i-2]
            elif arr[i-1]==0: # 바로 앞이 0인 경우
                result = dp[i-1]
                dp[i]=dp[i-1]
            else:
                result+=dp[i-2] # 바로 앞에 있는 가짓수 + 앞앞에 있는 가짓 수
                dp[i]=result

if not impossible:
    print(dp[length-1] % 1000000)





