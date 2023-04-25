from heapq import heappop, heappush
n = int(input())
room = []
for _ in range(n):
    s, e = map(int, input().split())
    room.append((s,e))

room.sort()

result=1
heap=[]
for s, e in room:
    if not heap:
        heappush(heap, e)
        continue
    else:
        if heap[0]<=s:
            heappop(heap)
        else:
            result += 1
        heappush(heap, e)

print(result)


