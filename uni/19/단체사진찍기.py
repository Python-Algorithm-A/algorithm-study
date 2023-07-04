from itertools import permutations
n = 2
data = ["M~C<2", "C~M>1"]

permu = list(map(list, permutations(['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'],8)))

result=0
for p in permu:
    for d in data:
        c1, c2, r, num = d[0], d[2], d[3], d[4]
        num = int(num)

        if r=='=':
            if abs(p.index(c1)-p.index(c2))-1 != num:
                result+=1
                break
        elif r=='>':
            if abs(p.index(c1)-p.index(c2))<=num+1:
                result+=1
                break
        else:
            if abs(p.index(c1)-p.index(c2))>=num+1:
                result+=1
                break

print(len(permu)-result)



