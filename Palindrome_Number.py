
t=int(input())
for i in range(1,t+1):
    n=int(input())
    s=0
    c=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if c==s:
        print("True")
    else:
        print("False")
    