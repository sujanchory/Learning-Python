def Col(i):
    if i%2:
      return i*3+1
    return i//2   

i=int(input())
print(i,end=" ")
while(i:=Col(i)):
    print(i,end=" ")
    if i==1:
        break
