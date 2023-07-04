import sys
input = sys.stdin.readline

n = int(input())
g=[]
result=0

for _ in range(n):
    g.append(list(map(int, input().split())))

def dfs(status, x, y):
    global result

    if x==n-1 and y==n-1:
        result+=1
        return

    if status=='가로':
        nx = x
        ny = y+1

        if nx>=0 and nx<n and ny>=0 and ny<n:
            if g[nx][ny]==0:
                dfs('가로', nx, ny)

        nx = x+1
        ny = y+1

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if g[nx][ny]==0 and g[x][ny]==0 and g[nx][y]==0:
                dfs('대각선', nx, ny)


    elif status=='세로':
        nx = x+1
        ny = y

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if g[nx][ny]==0:
                dfs('세로', nx, ny)

        nx = x+1
        ny = y+1

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if g[nx][ny]==0 and g[x][ny]==0 and g[nx][y]==0:
                dfs('대각선', nx, ny)

    else:
        nx = x
        ny = y + 1

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if g[nx][ny] == 0:
                dfs('가로', nx, ny)

        nx = x + 1
        ny = y + 1

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if g[nx][ny] == 0 and g[x][ny] == 0 and g[nx][y] == 0:
                dfs('대각선', nx, ny)

        nx = x + 1
        ny = y

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if g[nx][ny] == 0:
                dfs('세로', nx, ny)

dfs('가로', 0, 1)
print(result)