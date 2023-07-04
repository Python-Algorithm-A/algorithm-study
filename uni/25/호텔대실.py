from heapq import heappop, heappush

def solution(book_time):
    answer = 1

    # "HH:MM" → HH * 60 + MM
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()
    print(book_time_ref)

    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap, e)
            continue
        if heap[0] <= s: # 가장 마감시간이 빠른 호텔의 마감시간보다 현재 예약 시작이 늦는 경우
            heappop(heap)
        else:
            answer += 1 # 호텔방 추가
        heappush(heap, e + 10)

    return answer
