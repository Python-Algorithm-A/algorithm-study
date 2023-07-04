from collections import deque


def solution(board):
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]

    # R위치 찾기
    for i in range(len(board)):
        if "R" in board[i]:
            rx = i
            ry = board[i].index("R")

    q = deque()
    q.append((rx, ry, 0))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # BFS
    while q:
        k = q.popleft()

        x = k[0]
        y = k[1]
        cnt = k[2]

        if board[x][y] == 'G': # 도달
            return cnt

        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m: # 벽일 때
                    nx -= dx[i]
                    ny -= dy[i]
                    if not visited[nx][ny]:
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = True
                    break
                elif board[nx][ny] == 'D': # 장애물일 때
                    nx -= dx[i]
                    ny -= dy[i]
                    if not visited[nx][ny]:
                        q.append((nx, ny, cnt + 1))
                        visited[nx][ny] = True
                    break
    return -1

