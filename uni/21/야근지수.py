# heapq 사용
# 가장 큰 수 뽑아서 -1 하면 됨

import heapq

n=4
works=[4, 3, 3]

if sum(works)<n:
        print(0)
else:
    result=0
    works = [-w for w in works]
    heapq.heapify(works)

    while n>0:
        max_value = heapq.heappop(works) # 가장 작은 것을 추출
        heapq.heappush(works, max_value+1) # 하나 빼서 다시 넣어줌
        n-=1

    for i in range(len(works)):
            result+=works[i]**2
    print(result)

