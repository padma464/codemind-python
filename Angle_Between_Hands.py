n=input()
n=n.split(":")
n[0]=int(n[0])
n[1]=int(n[1])
h=n[0]*30+(n[1]/2)
m=n[1]*6
a=abs(h-m)
b=abs(360-a)
if a<b:
    print(a)
else:
    print(b)