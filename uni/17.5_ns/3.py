paper = list(map(int, input().split()))
n = int(input())

def f(arr, n):
    value = max(arr)
    idx = arr.find(value)

    # 왼쪽
    left_num = idx-1


    # 오른쪽
    i = idx
    cnt=1

    while i<=len(arr-1):
        i+=2



