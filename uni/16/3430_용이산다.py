from collections import deque
import sys
input = sys.stdin.readline

d=True
case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    result=[]
    q=deque()
    d=True
    for i in range(m):
        if arr[i]==0:
            q.append(i)
    if arr[0]!=0:
        d=False

    for i in range(m):
        hosu = arr[i]
        if hosu!=0:
            if q:
                result.append(hosu)
            else:
                d=False
                break
    for i in range(arr.count(0)-len(result)):
        result.append(0)
    if d==False:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))


