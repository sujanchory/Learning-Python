n=list(map(int,input().split()))
odd,even=0,0
for i in range(len(n)):
    if n[i]%2==0:
        even+=n[i]
    else:odd+=n[i]
print(odd,even)

