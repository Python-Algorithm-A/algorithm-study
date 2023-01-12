import sys
sys.setrecursionlimit(10**7) # 제귀 허용치를 넓혀줌
input = sys.stdin.readline

n, m = map(int,input().split()) # 정점의 갯수, 간선의 갯수
arr = [[] *(n+1) for _ in range(n+1)] # 2차원 배열 초기화
visited=[False] * (n+1)
count=0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(k):
    visited[k] = True # 방문 체크
    for num in arr[k]: # 해당 노드에 (바로) 연결되어 있는 노드 탐색
        if not visited[num]: # 방문하지 않은 노드라면 탐색
            dfs(num)


for i in range(1, n+1): # 1부터 노드를 탐색
    if not visited[i]: # 방문하지 않은 노드라면 count++ (새로운 연결노드이므로)
        count+=1
        dfs(i)


print(count)


