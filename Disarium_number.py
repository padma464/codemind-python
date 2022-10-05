n=input()
le=len(n)
n=int(n)
num=n
i=le
result=0
while n>0:
    r=n%10
    result=result+pow(r,i)
    n=int(n/10)
    i=i-1
if(num==result):
    print("True")
else:
    print("False")