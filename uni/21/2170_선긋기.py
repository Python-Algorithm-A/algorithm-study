import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

start = arr[0][0]

for s,e in arr:
    if s<=start and e>=start:
        start = e

print(start)
print(start-arr[0][0])
