def fact(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
n=int(input())
b=0
t=n
while n>0:
    r=n%10
    n=n//10
    b=b+fact(r)
if t==b:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")