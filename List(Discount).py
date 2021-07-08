p=list(map(int,input().split()))
d=list()
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]>=p[j]:
            d.append(p[i]-p[j])
            break
    else:
        d.append(p[i])
print(d)
