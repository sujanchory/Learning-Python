a=list(map(int,input().split()))
#a.sort()
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
