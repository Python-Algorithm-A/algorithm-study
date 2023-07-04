n = int(input())
T = []
for _ in range(n):
    T.append(list(input().split()))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

result="YES"


def track():
    for x in range(n):
        for y in range(n):
            if T[x][y]=='T':
                for d in range(4):
                    nx = x
                    ny = y
                    while nx<n-1 and nx>-1 and ny>-1 and ny<n-1:
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if T[nx][ny] == 'O':
                            break
                        elif T[nx][ny] == 'S':
                            return True
                            break

    return False


def install(start_i, start_j, obstacle):
    global result
    if obstacle==3:
        if track():
            result = "NO"
        return

    for i in range(start_i, n):
        for j in range(start_j, n):
            if T[i][j] == 'X':
                T[i][j] = 'O'
                install(i, j, obstacle+1)
                T[i][j] = 'X'

install(0 ,0, 0)
print(result)