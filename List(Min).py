a=list(map(int,input().split()))
    ##a.sort()
    ##print(a[0])
m=0
for i in a:
    if i>m:
        m=i
print(m)

m=a[0]
for i in a:
    if i<m:
        m=i
print(m)

