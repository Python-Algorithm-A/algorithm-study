source = input()

arr = [0]*26

result = []
for i in range(len(source)):
    arr[ord(source[i])-97] += 1

for _ in range(max(arr)):
    for i in range(26):
        if arr[i] >= 1:
            arr[i] -= 1
            result.append(chr(i+97))

for r in result:
    print(r, end='')