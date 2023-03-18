import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
result=0
last = matrix[n-1][1]
for i in range(n-2, -1, -1):
    result += matrix[i][0] * matrix[i][1] * last
print(result)