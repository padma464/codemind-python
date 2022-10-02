def hcf(a,b):
    if a>b:
        h=a
        s=b
    else:
        h=b
        s=a
    for i in range(h,0,-1):
        if h%i==0:
            if s%i==0:
                return i
n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    k=hcf(k,i)
print(k)