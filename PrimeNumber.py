n=int(input())
f=0
for i in range(1,n+1):
    if (n%i==0):
        f+=1
    else:
        continue
if(f<=2):
    print("Prime")
else:
    print("NOt A Prime")
