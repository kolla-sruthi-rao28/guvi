n1=int(input())
a=n1
s=0
while(n1!=0):
    temp=n1%10
    s=s+temp*temp*temp
    n1=int(n1/10)
   
if(s==a):
    print("yes")
else:
    print("no")    
