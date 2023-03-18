# 크루스칼 알고리즘 사용
# (그래프 내의 모든 정점들을 가장 적은 비용으로 연결)

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 간선의 비용을 기준으로 오름차순
    link = set([costs[0][0]])
    print(link)

    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link: # 두 노드 모두 지나갔다면 pass
                continue
            if v[0] in link or v[1] in link: # 두 노드 중 하나만 지나갔다면 연결
                link.update([v[0], v[1]])
                print(link)
                answer += v[2]
                break
    print(answer)
    return answer


solution(6, [[0,1,1],[1,2,3],[2,3,2],[4,5,1],[1,4,5],[0,5,7]])