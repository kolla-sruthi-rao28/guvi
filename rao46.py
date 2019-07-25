n12=int(input())
m=list(map(int,input().split(" ")))
d={}
for key1 in m:
    d[key1]=m.count(key1)

l=[]
for key1,values in d.items():
    if(d[key1]==1):
        print(key1)
        break
