n=int(input())
f=0
for i in range(2,n):
    if (n%i==0):
      print(n,"is not Prime")
      break
else:
  print(n,"is Prime")
    
