n1=int(input())
m1=list(map(int,input().split(" ")))
l=[]
for i in range(len(m1)):
    if(i==m1[i]):
        l.append(i)
if l==[]:
   print("-1")
else:        
  l.sort()
  for i in l:
    print(i,end=" ")       
