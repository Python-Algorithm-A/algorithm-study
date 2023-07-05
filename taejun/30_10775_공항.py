import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

G = int(input())
P = int(input())

gate = [i for i in range(G+1)]
ans = 0
def find(g_i):
	if gate[g_i] == g_i:
		return g_i
	else:
		gate[g_i] = find(gate[g_i])
		return find(gate[g_i])

for _ in range(P):
	temp = find(int(input()))
	print(gate)
	if temp == 0:
		break
	ans +=1
	gate[temp] -= 1
	print(gate)


print(ans)
'''
import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

gate = [i for i in range(G+1)]
ans = 0
for _ in range(P):
	g_i = int(input())
	next_gate = gate[g_i]
	if next_gate == 0:
		break
	else:
		ans += 1
	
	left = g_i
	while(gate[left] == next_gate):
		left -= 1
	for i in range(left+1, G+1):
		if gate[i] != next_gate:
			break
		else:
			gate[i] = gate[left]
	
print(ans)
'''