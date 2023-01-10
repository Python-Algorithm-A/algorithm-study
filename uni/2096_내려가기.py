import sys
input = sys.stdin.readline

n = int(input()) # 줄의 갯수
arr=[]
for _ in range(n):
    x, y, z = map(int,input().split())
    arr.append(x)
    arr.append(y)
    arr.append(z)

# x,y,z의 값을 첫째줄의 수로 초기화
x_min, y_min, z_min = arr[0], arr[1], arr[2]
x_max, y_max, z_max = arr[0], arr[1], arr[2]


for i in range(2,n+1):
    num = 3*i-1 # 줄의 가장 오른쪽 인덱스

    rx_max = arr[num-2]
    rx_max += max(x_max, y_max)
    rx_min = arr[num-2]
    rx_min += min(x_min, y_min)

    ry_max = arr[num-1]
    ry_max += max(x_max, y_max, z_max)
    ry_min = arr[num - 1]
    ry_min += min(x_min, y_min, z_min)

    rz_max = arr[num]
    rz_max += max(y_max, z_max)
    rz_min = arr[num]
    rz_min += min(y_min, z_min)
    x_max, y_max, z_max = rx_max, ry_max, rz_max
    x_min, y_min, z_min = rx_min, ry_min, rz_min

print(max(x_max, y_max, z_max))
print(min(x_min, y_min, z_min))
