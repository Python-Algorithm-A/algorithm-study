n = 4
l = 30
r = 118

arr="11011"
for i in range(n-1):
    new_arr=""
    for j in range(len(arr)):
        if arr[j]=="1":
            new_arr+="11011"
        else:
            new_arr+="00000"
    arr = new_arr

cnt=0
for i in range(l-1, r):
    if arr[i]=="1":
        cnt+=1
print(cnt)

