
n = int(input())

result=0
# def primes_sieve(limit):
#     is_prime = [True] * limit
#     is_prime[0] = is_prime[1] = False
#     for i in range(2, int(limit**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i**2, limit, i):
#                 is_prime[j] = False
#     return [i for i in range(limit) if is_prime[i]]
# prime = primes_sieve(n+1)

# 에라토스테네스의 체
# 소수를 대량으로 빠르게 구현
#
prime = [False, False] + [True] * (n-1)
prime_num = []

for i in range(2, n+1):
    if prime[i]:
        prime_num.append(i)
        for j in range(2*i, prime+1, i):
            prime[j] = False


if n==1:
    print(0)
else:
    s=0
    e=0
    su=prime[0]
    while s<=e:
        if su==n:
            result+=1
            e += 1
            if e >=len(prime):
                break
            su += prime[e]

        elif su<n:
            e+=1
            if e>=len(prime):
                break
            su+=prime[e]
        else:
            su-=prime[s]
            s+=1

    print(result)