n=list(map(int,input().split()))
c=len(n)
for i in range(len(n)-1,-1,-1):
    if n[i]==0:
        n.insert(i+1,0)
    if len(n)>c:
        n.pop()
print(n)
