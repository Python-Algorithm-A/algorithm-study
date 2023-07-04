import sys
input = sys.stdin.readline

n, m, h = map(int, input().split()) # 세로선, 가로선, 가로선을 놓을 수 있는 갯수

# 2차원 배열 초기화
d = [[0] * (n+1) for _ in range(h+1)]

# 고정 사다리 넣기
for _ in range(m):
    a, b = map(int, input().split())
    d[a][b]=1

# 사다리 타기
def game():
    for num in range(1, n+1):
        temp=num
        for i in range(1, h+1): # 아래로 한 칸씩 내려감
            if d[i][temp]: # 오른쪽으로 이동
                temp+=1
            elif d[i][temp-1]==1: # 왼쪽으로 이동
                temp-=1
        if num!=temp: # i번째 -> i번째가 나오지 않으면
            return False
    return True

# 사다리를 놓을 수 있는지
def can_install(x, y):
    if y == n: # 맨 끝 사다리
        return False

    if y == 1: # 첫번째 사다리
        if d[x][y + 1] == 1:
            return False
    else:
        if d[x][y + 1] == 1 or d[x][y - 1] == 1:  # 양 옆에 사다리가 1개라도 있을 경우
            return False
    return True


def addWidth(lv, start_idx): # start_idx를 기억함으로써 조합가능
    global answer

    if lv > 3 or lv > answer:
        return

    if game():
        answer = min(answer, lv)

    for i in range(start_idx, h + 1):
        for j in range(1, n + 1):
            if d[i][j] == 1:
                continue
            if can_install(i, j):
                d[i][j] = 1
                addWidth(lv + 1, i)
                d[i][j] = 0
    return 0

answer = 4
addWidth(0 ,1)
if answer==4:
    print(-1)
else:
    print(answer)


