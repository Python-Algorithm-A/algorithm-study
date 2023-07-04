def solution(scores):
    answer = 0
    wh = scores[0]
    wh_sum = sum(wh)

    # 정렬
    scores.sort(key = lambda x: (-x[0], x[1]))
    before=0
    for score in scores:
        # 완호가 인센티브를 받지x
        if wh[0]<score[0] and wh[1]<score[1]:
            return -1

        # 완호 외 인센티브를 못받는 사람 건너 뛰기
        if before <= score[1]:
            if wh_sum < sum(score): # 완호보다 점수가 높으면 +1
                answer+=1
            before = score[1]
    return answer
