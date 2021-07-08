a=list(map(int,input().split()))
b=list(map(int,input().split()))

##a.extend(b)
##d=set(a)
##c=list(d)
##print(c)

for i in b:
    if i not in a:
        a.append(i)
print(a)
    
