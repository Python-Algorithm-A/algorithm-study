import sys

sys.setrecursionlimit(10 ** 9)

INF = 1e9
result = INF

def solution(board):
    n = len(board)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y, d, money, rute):
        global result

        if x == n - 1 and y == n - 1:
            result = min(result, money)
            return

        if result < money:
            return

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if board[nx][ny] == 0 and (nx, ny) not in rute:
                    if i == d or i == (d + 2) % 4:
                        rute.append((nx, ny))
                        dfs(nx, ny, i, money + 100, rute)
                        rute.pop()

                    else:
                        rute.append((nx, ny))
                        dfs(nx, ny, i, money + 600, rute)
                        rute.pop()

    dfs(0, 0, 1, 0, [(0, 0)])
    dfs(0, 0, 2, 0, [(0, 0)])

    return result