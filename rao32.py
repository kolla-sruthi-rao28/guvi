s12=input()
j=0
for i in range(len(s12)):
    if(s12[j]<s12[i]):
        print(s12[i:])
        break
