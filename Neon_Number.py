n=int(input())
c=n
s=0
n=n**2
while n>0:
    r=n%10
    s=s+r
    n=n//10
if(s==c):
    print("Neon Number")
else:
    print("Not Neon Number")