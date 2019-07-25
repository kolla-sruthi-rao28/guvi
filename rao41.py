n1=int(input())
m12=list(map(int,input().split(" ")))
d={}
for key in m12:
    d[key]=m12.count(key)

l=[]
for key,values in d.items():
    if(d[key]>1):
        l.append(key)
        
if l==[]:
    print("unique") 
else:       
  l.sort()
  for i in l:
    print(i,end=" ")
