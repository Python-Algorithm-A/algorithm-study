import sys
input = sys.stdin.readline

n, m, c = map(int,input().split())
w=[]
for _ in range(c):
    w.append(list(map(int,input().split())))

a = [0] + list(map(int,input().split()))
b = [0] + list(map(int,input().split()))

# d[i][j] -> i가 j과 악수를 시도할 때 까지의 최대값
d = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 악수, 전 사람과 악수, 악수x
        d[i][j] = max(max(d[i-1][j-1] + w[a[i]-1][b[j]-1], d[i][j-1]), d[i-1][j])

print(d[n][m])
