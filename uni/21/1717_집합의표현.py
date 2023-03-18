# 유니온 파인드

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(k):
    if k != parent[k]:
        parent[k] = find(parent[k])
    return parent[k]

def union(x, y):
    x = find(x)
    y = find(y)

    if x!=y:
        if x<y: parent[y]=x
        else: parent[x]=y

for _ in range(m):
    a, b, c = map(int, input().split())

    if a==0: # Union 과정
        union(b,c)
    else: # Find 과정
        if find(parent[b]) == find(parent[c]):
            print("YES")
        else:
            print("NO")
