n=list(map(int,input().split()))
m=list()
for i in range(0,len(n),2):
    for j in range(n[i]):
         m.append(n[i+1])
print(m)
