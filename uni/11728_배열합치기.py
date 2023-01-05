n, m = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
result=[]

i=0 # arrA 배열 포인터
j=0 # arrB 배열 포인터

while True:
    if i>=n or j>=m: # 두 배열 중 하나라도 끝에 닿으면
        if i>=n and j<m:
            result.extend(arrB[j:])
        elif i<n and j>=m:
            result.extend(arrA[i:])
        break # 두 배열 모두 끝 점에 닿는 경우

    # 포인터가 가리키는 숫자를 비교
    if arrA[i]> arrB[j]:
        result.append(arrB[j])
        j+=1
    else:
        result.append(arrA[i])
        i+=1

for x in result:
    print(x, end=' ')


