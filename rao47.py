n11=int(input())
s=0
for i in range(2,n11):
    flag=1
    for j  in range(2,i):
        if(i%j==0):
            flag=0
            break
    if(flag):
        k=str(i)
        l=[]
        for m in range(len(k)):
            l.append(k[m])
        if(l[-1]=='3'):
            s=s+i
print(s)       
