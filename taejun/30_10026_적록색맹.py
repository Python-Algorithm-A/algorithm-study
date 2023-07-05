import sys
input = sys.stdin. readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
grids =[]
regions = [[0 for _ in range(N)] for _ in range(N)]
region = 0
region_disease = 0
for _ in range(N):
	grids.append(input())

def set_region(i, j, region):
	regions[i][j] = region
	
	if i>0:
		if regions[i-1][j] == 0 and grids[i-1][j] == grids[i][j]:
			set_region(i-1,j,region)
	if i<N-1:
		if regions[i+1][j] == 0 and grids[i+1][j] == grids[i][j]:
			set_region(i+1,j,region)
	if j>0:
		if regions[i][j-1] == 0 and grids[i][j] == grids[i][j-1]:
			set_region(i,j-1,region)
	if j<N-1:
		if regions[i][j+1] == 0 and grids[i][j] == grids[i][j+1]:
			set_region(i,j+1,region)


for i in range(N):
	for j in range(N):
		if regions[i][j] == 0:
			region += 1
			set_region(i, j, region)

regions = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
	grids[i] = grids[i].replace('G', 'R')
for i in range(N):
	for j in range(N):
		if regions[i][j] == 0:
			region_disease += 1
			set_region(i, j, region_disease)


print(region, region_disease)