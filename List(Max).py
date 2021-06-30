a=list(map(int,input().split()))
    ##a.sort()
    ##print(a[-1])
m=0
for i in a:
    if i>m:
        m=i
print(m)
