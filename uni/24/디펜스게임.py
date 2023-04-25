# 힙 사용
# 만약 적의 수가 모자라다면, 현재까지 적대했던 적 중 가장 많은 수의 적에게 무적권을 사용

from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []

    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e 
        if sumEnemy > n: # 현재의 병사로 적을 물리칠 수 없다면
            if k == 0: break # 무적권을 다 써버렸다면 끝
            sumEnemy += heappop(heap) # 적대했던 적 중 가장 많은 적에게 무적권 사용
            k -= 1 # 무적권 하나 사용
        answer += 1 # 라운드 통과
    return answer



