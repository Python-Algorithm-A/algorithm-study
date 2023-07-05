import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

city = []
for _ in range(N):
	city.append(list(map(int, input().split())))
plan = list(map(int, input().split()))	

connected_city = [0 for _ in range(N+1)]
def able_visit(i):
	connected_city[i] = 1

	for j in range(N):
		if city[i-1][j] ==1:
			if connected_city[j+1] == 0:
				able_visit(j+1)

able_visit(plan[0])

ans = "YES"
for i in range(M):
	if connected_city[plan[i]] == 0:
		ans = "NO"
print(ans)


