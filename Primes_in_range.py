from math import sqrt
def isprime(n):
    if n==0 or n==1:
        return 0
    else:
        sq=int(sqrt(n))
        for i in range(2,sq+1):
            if n%i==0:
                return 0
                break
        return 1
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if(isprime(i)==1):
        c+=1
print(c)