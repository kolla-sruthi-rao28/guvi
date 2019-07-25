s2=input()
s1=input()
l=[]
for i in s1:
    l.append(i)
if(len(s1)==len(s2)):
   for i in range(len(s2)):
       k=ord(s2[i])-ord('a')+1
       l[i]=ord(s1[i])+k
for i in l:
   if i>ord('z'):
       i=i-ord('z')+ord('a')-1
   print(chr(i),end="")   
