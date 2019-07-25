s1,e=input().split(" ")
s1=int(s1)
e=int(e)
for n in range(s1+1,e):
    f=1
    for i in range(2,n):
        if(n%i==0):
            f=0
            break
    if(f):
        print(n,end=" ")
