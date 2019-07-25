n1=int(input())
m1=list(map(int,input().split(" ")))
d={}
for key in m1:
    d[key]=m1.count(key)

l=[]
for key,values in d.items():
    if(d[key]==1):
        print(key)
        break

