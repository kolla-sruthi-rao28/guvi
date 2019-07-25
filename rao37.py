n=int(input())
me=[]*n
for i in range(0,2**n):
    k2=[]
    for j in range(n-1,0,-1):
        k2.append(int(i/2**j)%2)
    k2.append(i%2)    
    me.append(k) 
    
for i in  m:
    s=''
    for j in i:
        j=str(j)
        s=s+j
    print(s)    
