n12=int(input())
m=[]*n12
for i in range(0,2**n12):
    k=[]
    for j in range(n12-1,0,-1):
        k.append(int(i/2**j)%2)
    k.append(i%2)    
    m.append(k) 
    
for i in  m:
    s=''
    for j in i:
        j=str(j)
        s=s+j
    print(s) 
