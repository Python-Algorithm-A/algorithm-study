music = [1]
plus = list(map(int,input().split()))
music += plus

n = len(music)

result=0

for i in range(1, n):

    s = music[i-1]
    e = music[i]

    if s>music[i]:
        e=s
        s=music[i]
    else:
        e=music[i]

    while s!=e:

        if abs(s-e)==1:
            result+=1
            s+=1
            print(s, e)
            break

        if s<7 and s%2!=0:
            s+=2

        elif s<7 and s%2==0:
            s+=1

        elif s>7 and s%2==0:
            s+=2

        elif s>=7 and s%2!=0:
            s+=1
        result += 1

print(result)



