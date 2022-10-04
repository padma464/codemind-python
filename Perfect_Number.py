def perfect(n):
    c=n
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if c==s:
        return True
    else:
        return False
n=int(input())
if perfect(n):
    print("True")
else:
    print("False")