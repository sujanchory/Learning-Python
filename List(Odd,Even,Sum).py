n=list(map(int,input().split()))
odd=0
even=0
for i in n:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(odd,even)
