h=list(map(int,input().split()))
s=h.copy()
h.sort()
c=0
for i in range(len(h)):
    if h[i]!=s[i]:
        c+=1
print(c)
