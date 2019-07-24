s,q=map(int,input().split())
p=list(map(int,input().split()))
count=0
for i in range(len(p)):
  for j in range(i+1,len(p)):
    if(p[i]+p[j]==q):
        count=1
        break
if(count):
   print("yes")
else:
   print("no")    
        
