st,e1=input().split(" ")
st=int(st)
e1=int(e1)
for n in range(st+1,e1):

    a=n
    s=0
    while(n!=0):
        temp=n%10
        s=s+temp*temp*temp
        n=int(n/10)
   
    if(s==a):
        print(a)
