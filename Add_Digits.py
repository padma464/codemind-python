def sim(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input())
s=sim(n)
while s>9:
    s=sim(s)
print(s)
    