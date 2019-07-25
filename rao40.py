n1=int(input())
m12=list(map(int,input().split(" ")))
l=[]
while(len(m12)!=0):
   if len(m12)>1: 
    l.append(max(m12))
    l.append(min(m12))
    m12.remove(max(m12))
    m12.remove(min(m12))
   else:
       l.append(max(m12))
       m12.remove(max(m12))
for i in l:
     print(i,end=" ")  
